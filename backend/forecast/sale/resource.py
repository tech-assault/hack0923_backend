from import_export import resources, fields, widgets

from .models import Category, Sale, Store


class CategoryResource(resources.ModelResource):
    sku = fields.Field(attribute='sku', column_name='pr_sku_id')
    group = fields.Field(attribute='group', column_name='pr_group_id')
    category = fields.Field(attribute='category', column_name='pr_cat_id')
    subcategory = fields.Field(attribute='subcategory',
                               column_name='pr_subcat_id')
    uom = fields.Field(attribute='uom', column_name='pr_uom_id')

    class Meta:
        import_id_fields = ('sku',)
        model = Category


class SaleResource(resources.ModelResource):
    store = fields.Field(
        attribute='store', column_name='st_id',
        widget=widgets.ForeignKeyWidget(Store, field='store'))
    sku = fields.Field(
        attribute='sku', column_name='pr_sku_id',
        widget=widgets.ForeignKeyWidget(Category, field='sku'))
    sales_type = fields.Field(attribute='sales_type',
                              column_name='pr_sales_type_id')
    sales_units = fields.Field(attribute='sales_units',
                               column_name='pr_sales_in_units')
    sales_units_promo = fields.Field(attribute='sales_units_promo',
                                     column_name='pr_promo_sales_in_units')
    sales_rub = fields.Field(attribute='sales_rub',
                             column_name='pr_sales_in_rub')
    sales_run_promo = fields.Field(attribute='sales_run_promo',
                                   column_name='pr_promo_sales_in_rub')

    class Meta:
        exclude = ('id',)
        import_id_fields = ('store', 'sku', 'date')
        model = Sale


class StoreResource(resources.ModelResource):
    store = fields.Field(attribute='store', column_name='st_id')
    city = fields.Field(attribute='city', column_name='st_city_id')
    division = fields.Field(attribute='division',
                            column_name='st_division_code')
    type_format = fields.Field(attribute='type_format',
                               column_name='st_type_format_id')
    loc = fields.Field(attribute='loc', column_name='st_type_loc_id')
    size = fields.Field(attribute='size', column_name='st_type_size_id')
    is_active = fields.Field(attribute='is_active', column_name='st_is_active')

    class Meta:
        import_id_fields = ('store',)
        model = Store
