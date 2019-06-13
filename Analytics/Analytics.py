import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# Analytics
#

class Analytics(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Analytics" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Developer"]
    self.parent.dependencies = []
    self.parent.contributors = ["Steve Pieper (Isomics, Inc.)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
This module tracks what you do in Slicer and reports it to Google (but only if you opt in).
"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """
This file was originally developed by Steve Pieper, Isomics, Inc. and was partially funded by NSF Advances in Biological Informatics Collaborative grant to Murat Maga (ABI-1759883).
""" # replace with organization, grant and thanks.

    # Tasks to execute after the application has started up
    slicer.app.connect("startupCompleted()", self.performPostModuleDiscoveryTasks)

  def reportToGoogle(self, module):
    baseURL = "http://192.168.0.209:8081" ;# for local testing
    baseURL = "https://pieper.github.io/SlicerAnalytics"
    self.webWidget.url = baseURL + "?utm_source=slicer&utm_medium=%s&utm_campaign=Analytics" % module
    print("Pinged: %s" % self.webWidget.url)

  def performPostModuleDiscoveryTasks(self):
    """ Give the user a chance to opt in or out
    """

    print("!"*80)
    print("You are being watched!!!")
    print("!"*80)

    self.webWidget = slicer.qSlicerWebWidget()
    slicer.util.mainWindow().statusBar().addWidget(self.webWidget)

    self.logic = AnalyticsLogic()
    self.logic.watchAndReport(self.reportToGoogle)

#
# AnalyticsWidget
#

class AnalyticsWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    # Add vertical spacer
    self.layout.addStretch(1)


  def cleanup(self):
    pass


#
# AnalyticsLogic
#

class AnalyticsLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  @staticmethod
  def enabled(onOff=None):
    settings = qt.QSettings()
    if onOff is None:
      if settings.contains("Analytics/enabled"):
        return settings.value("Analytics/enabled")
      else:
        return False
    else:
      settings.setValue("Analytics/enabled", onOff is True)

  def moduleSelected(self, moduleName):
    print("I saw you select %s" % moduleName)

  def watchAndReport(self, reporter):
    if not reporter:
      reporter = self.moduleSelected
    moduleSelector = slicer.util.findChildren(name="ModuleSelectorToolBar")[0]
    moduleSelector.connect("moduleSelected(QString)", reporter)


class AnalyticsTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    pass

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_Analytics1()

  def test_Analytics1(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests should exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("We don't have a test")
