from adapt.intent import IntentBuilder

from mycroft.skills.context import adds_context, removes_context
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'WeltgeistNull'

LOGGER = getLogger(__name__)


class OBD2CodesSkill(MycroftSkill):
    def __init__(self):
        super(OBD2CodesSkill, self).__init__(name="OBD2CodesSkill")

    # def initialize(self):
    #     pass

    @intent_handler(IntentBuilder('DiagnoseVehicleIntent') \
        .require('DiagnoseVehicleKeyword'))
    @adds_context('AskingForMakeContext')
    def handle_diagnose_vehicle_intent(self, message):
        self.speak("what make is your vehicle")


    @intent_handler(IntentBuilder('VehicleMakeIntent') \
        .require('AskingForMakeContext') \
        .require('VehicleMakeKeyword'))
    @removes_context('AskingForMakeContext')
    @adds_context('ConfirmVehicleMakeContext')
    def handle_vehicle_make_intent(self, message):
        make = message.data.get('VehicleMakeKeyword')
        self.speak("The vehicle make you have told me is: {}. Is this correct?".format(make))


    @intent_handler(IntentBuilder('ConfirmVehicleIntent') \
        .require('ConfirmVehicleMakeContext') \
        .require('ConfirmKeyword'))
    def handle_confirm_intent(self, message):
        user_confirm = message.data.get('ConfirmKeyword')
        self.speak("You said: {}".format(user_confirm))

    def stop(self):
        pass


def create_skill():
    return OBD2CodesSkill()
