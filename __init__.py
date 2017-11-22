from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'WeltgeistNull'

LOGGER = getLogger(__name__)

class OBD2CodesSkill(MycroftSkill):
    def __init__(self):
        super(OBD2CodesSkill, self).__init__(name="OBD2CodesSkill")

    def initialize(self):

        diagnose_vehicle_intent = IntentBuilder("DiagnoseVehicle"). \
            require("DiagnoseVehicleKeyword").build()
        self.register_intent(diagnose_vehicle_intent, self.handle_diagnose_vehicle_intent)

        # vehicle_make_intent = IntentBuilder("VehicleMakeIntent"). \
        #     require("VehicleMakeKeyword").build()
        # self.register_intent(vehicle_make_intent, self.handle_vehicle_make_intent)

    def handle_diagnose_vehicle_intent(self, message):
        self.speak_dialog("diagnose.vehicle")

    # def handle_vehicle_make_intent(self, message):
    #     self.speak_dialog("vehicle.make")

    def stop(self):
        pass


def create_skill():
    return OBD2CodesSkill()
