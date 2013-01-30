from plone.app.registry.browser import controlpanel

from collective.regexredirector.interfaces import IRegexSettings, _


class RegexSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IRegexSettings
    label = _(u"Redirect Regex settings")
    description = _(u"""""")

    def updateFields(self):
        super(RegexSettingsEditForm, self).updateFields()
        

    def updateWidgets(self):
        super(RegexSettingsEditForm, self).updateWidgets()

class RegexSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = RegexSettingsEditForm
