import json

from django.contrib import admin
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render

from import_export.admin import ImportExportModelAdmin

from .models import Category, Forecast, Sale, Store, SaleOfSKUInStore
from .resources import CategoryResource, StoreResource, SaleResource
from .utils import ImportUtils


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    """Административная панель для модели Category."""
    resource_class = CategoryResource

    list_display = ("sku", "group", "category", "subcategory", "uom")


@admin.register(Store)
class StoreAdmin(ImportExportModelAdmin):
    """Административная панель для модели Store."""
    resource_class = StoreResource

    list_display = ("store", "city", "division", "type_format", "loc", "size",
                    "is_active")


@admin.register(Sale)
class SaleAdmin(ImportExportModelAdmin):
    """Административная панель для модели Sale."""
    resource_class = SaleResource

    list_display = ("store", "sku")

    def import_action(self, request):
        import_sale = []
        import_sale_of_sku_in_store = []
        indexs_of_store_sku = {}
        create_new_sale = []
        create_new_sale_of_sku_in_store = []
        if request.method == "POST":

            # capture payload from request
            csv_file = json.loads(request.POST.get("file_name"))
            reader = json.loads(request.POST.get("rows"))
            column_headers = json.loads(request.POST.get("csv_headers"))
            print(column_headers)
            util_obj = ImportUtils(column_headers)
            index = 0
            for row in reader:
                print(row)
                store = row[util_obj.get_column("st_id")]
                sku = row[util_obj.get_column("pr_sku_id")]

                info_of_store_sku_sale = {
                    'date': row[util_obj.get_column("date")],
                    'sales_type': row[util_obj.get_column("pr_sales_type_id")],
                    'sales_units': row[
                        util_obj.get_column("pr_sales_in_units")],
                    'sales_units_promo': row[util_obj.get_column(
                        "pr_promo_sales_in_units")],
                    'sales_rub': row[util_obj.get_column("pr_sales_in_rub")],
                    'sales_run_promo': row[util_obj.get_column(
                        "pr_promo_sales_in_rub")]
                }

                store_sku = (store, sku)
                if store_sku not in indexs_of_store_sku:
                    create_new_sale.append(Sale(store_id=store, sku_id=sku))
                    indexs_of_store_sku[store_sku] = index
                    index += 1

                    import_sale.append(
                        {"store": store, "sku": sku, "status": "FINISHED",
                         "msg": "Sale created successfully!"})
                create_new_sale_of_sku_in_store.append(
                    (store_sku, info_of_store_sku_sale))

            sale_from_db = Sale.objects.bulk_create(create_new_sale)
            sale_of_sku_in_store_from_db = SaleOfSKUInStore.objects.create(
                [
                    SaleOfSKUInStore(
                        sale_id=sale_from_db[indexs_of_store_sku[store_sku]],
                        **info_of_store_sku_sale)
                    for store_sku, info_of_store_sku_sale
                    in create_new_sale_of_sku_in_store]
            )

            context = {
                "file": csv_file,
                "entries": len(import_sale),
                "results": import_sale
            }
            return HttpResponse(json.dumps(context),
                                content_type="application/json")
        form = CsvImportForm()
        context = {"form": form, "form_title": "Upload users csv file.",
                   "description": "The file should have following headers: "
                                  "[NAME,HEIGHT,MASS,HAIR COLOR,EYE COLOR,SKIN COLOR,BIRTH YEAR,GENDER]."
                                  " The Following rows should contain information for the same.",
                   "endpoint": "/admin/sale/sale/import/"}
        return render(
            request, "admin/import_sale.html", context
        )

        # global variables to improve performance

    export_qs = None
    total_count = 0
    characters = []

    def export_action(self, request):
        if request.method == 'POST':
            offset = json.loads(request.POST.get('offset'))
            limit = json.loads(request.POST.get('limit'))
            self.characters = []
            if not self.export_qs:
                self.export_qs = models.Characters.objects.all().values_list(
                    "name", "height", "mass", "birth_year", "gender")

            for obj in self.export_qs[offset:limit]:
                self.characters.append({
                    "name": obj[0],
                    "height": obj[1],
                    "mass": obj[2],
                    "birth_year": obj[3],
                    "gender": obj[4]
                })

            context = {
                "results": self.characters
            }
            return HttpResponse(json.dumps(context),
                                content_type="application/json")

        # define the queryset you want to export and get the count of rows
        self.total_count = models.Characters.objects.all().count()
        context = {"total_count": self.total_count,
                   "form_title": "Export Characters to csv file",
                   "description": "",
                   "headers": ["Name", "Height", "Mass", "Birth Year",
                               "Gender"],
                   "endpoint": "/admin/starwars/characters/export/",
                   "fileName": "starwars_characters"}
        return render(
            request, "admin/export_sale.html", context
        )


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    """Административная панель для модели Forecast."""

    list_display = ("store", "sku", "forecast_date")
