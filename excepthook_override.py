import sys
import maya.cmds as cmds
utils = sys.modules['maya.utils']
script_name = "script_name"

class Except():
	"""
	Exception class
	"""
    def excepthook(self, tb_type, exc_object, tb, detail=2):
		"""
		Exception hook override for maya
		"""
        print utils.formatGuiException(tb_type, exc_object, tb, detail)
        cmds.ScriptEditor()
        errormsg = utils.formatGuiException(tb_type, exc_object, tb, detail)
        result = cmds.promptDialog(
                        title='Oh no a crash!',
                        message='Send feedback to devs:',
                        button=['OK', 'Cancel'],
                        defaultButton='OK',
                        cancelButton='Cancel',
                        dismissString='Ok')

        if result == 'OK':
            text = cmds.promptDialog(query=True, text=True)

        import sentry_sdk
        sentry_sdk.init(SENTRY_URL_HERE)
        sentry_sdk.capture_message(self.script_name + ' -- User feedback: ' + str(text) + " -- Error: " + errormsg)

    def run_excepthook(self, script):
		"""
		Run the override
		"""
        utils._guiExceptHook = self.excepthook
        self.script_name = script
