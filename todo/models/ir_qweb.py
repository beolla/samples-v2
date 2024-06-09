# -*- coding: utf-8 -*-
# from odoo import models
from odoo import models, fields, api
from . import assetsbundle


class IrQweb(models.AbstractModel):
    """ Add ``raise_on_code`` option for qweb. When this option is activated
    then all directives are prohibited.
    """
    _inherit = 'ir.qweb'

    def _get_asset_bundle(self, bundle_name, css=True, js=True, debug_assets=False, rtl=False, assets_params=None):
        files, external_assets = self._get_asset_content(bundle_name)

        return assetsbundle.AssetsBundleJsx(bundle_name, files, external_assets, env=self.env, css=css, js=js, debug_assets=debug_assets, rtl=rtl, assets_params=assets_params)
