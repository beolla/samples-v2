from odoo import models, fields, api
from odoo.addons.base.models.assetsbundle import AssetsBundle, JavascriptAsset, CompileError
from collections import OrderedDict
from subprocess import Popen, PIPE
import subprocess
from odoo.tools import misc
import logging
_logger = logging.getLogger(__name__)

def transpile_jsx(content_bundle):
    npm_root = subprocess.run(['npm', '-g', 'root'], text=True, capture_output=True)
    command = ['babel', '--presets', npm_root.stdout + '/@babel/preset-react', '--no-babelrc']
    try:
        compiler = Popen(command, stdin=PIPE, stdout=PIPE,
                         stderr=PIPE)
    except Exception:
        raise CompileError("Could not execute command %r" % command[0])
    (out, err) = compiler.communicate(input=content_bundle)
    if compiler.returncode:
        cmd_output = misc.ustr(out) + misc.ustr(err)
        if not cmd_output:
            cmd_output = u"Process exited with return code %d\n" % compiler.returncode
        raise CompileError(cmd_output)
    return out

class JsxAsset(JavascriptAsset):
    @property
    def content(self):
        # print('jsx asset content')
        content = super().content
        content = transpile_jsx(content.encode('utf-8')).decode('utf-8')
        print (content)
        return content

    

class AssetsBundleJsx(AssetsBundle):

    def __init__(self, bundle_name, files, external_assets, env, css=True, js=True, debug_assets=False, rtl=False, assets_params=None):
        super(AssetsBundleJsx, self).__init__(bundle_name, files, external_assets, env=env, css=css, js=js, debug_assets=debug_assets, rtl=rtl, assets_params=assets_params)
        for idx, js in enumerate(self.javascripts):
            # only run transpiler on our own custom script.
            # In production, a better way to distinguish jsx
            # script is needed. 
            if js.url.find('todo') >= 0:
                self.javascripts[idx] = JsxAsset(self, url=js.url, filename=js._filename, inline=js.inline)

    def js(self):
        """
        Override the base implementation to 
        run transpiler on js content, and re-save attachment.
        note that transpiler always run on the bundle
        This is a POC, and not intended for production.
        Further optimization needed 
        """ 
        # _logger.info('calling to js of ' + self.name )
        ira = super().js()
        return ira
        # try:
        #     content_bundle = self.transpile_jsx(ira.raw)
        #     extension = 'min.js' if is_minified else 'js'
        #     ir_attached = self.save_attachment(extension, content_bundle)
        #     return ir_attached[0]
        # except Exception as err:

        #     _logger.error(err)
        #     _logger.info(ira.raw.decode('utf-8'))
        #     return ira 
