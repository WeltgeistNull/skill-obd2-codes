from adapt.intent import IntentBuilder

from mycroft.skills.context import adds_context, removes_context
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'WeltgeistNull'

LOGGER = getLogger(__name__)

# TODO: Generalizable constructor for all of these Confirmation intents/contexts


class OBD2CodesSkill(MycroftSkill):
    '''Main OBD2 Codes skill handler'''

    def __init__(self):
        super(OBD2CodesSkill, self).__init__(name="OBD2CodesSkill")
        self.make = ""
        self.pid = ""

    def inquire(self, utterance):
        '''Wrapper for this skill's various inquries of the user.'''

        self.speak(utterance, expect_response=True)

    # def initialize(self):
    #     pass

    @intent_handler(IntentBuilder('DiagnoseVehicleIntent') \
        .require('DiagnoseVehicleKeyword').build())
    @adds_context('AskingForMakeContext')
    def handle_diagnose_vehicle_intent(self, message):
        self.inquire("what make is your vehicle?")


    @intent_handler(IntentBuilder('VehicleMakeIntent') \
        .require('AskingForMakeContext') \
        .require('VehicleMakeKeyword').build())
    @removes_context('AskingForMakeContext')
    @adds_context('AskPIDContext')
    def handle_vehicle_make_intent(self, message):
        make = message.data.get('VehicleMakeKeyword')
        self.inquire("""\
the vehicle make you have told me is: {}.\n\
what is your OBD-2 code?""".format(make))
        self.make = make


    @intent_handler(IntentBuilder('AskingForPIDIntent') \
        .require('AskPIDContext') \
        .require('PIDKeyword').build())
    @removes_context('AskPIDContext')
    @adds_context('ReadPIDDefinitionContext')
    def handle_ask_pid_intent(self, message):
        pid = message.data.get('PIDKeyword')
        self.pid = pid
        self.speak("the code you have told me is: {}".format(pid))


    # @intent_handler(IntentBuilder('ConfirmVehicleIntent') \
    #     .require('ConfirmVehicleMakeContext') \
    #     .require('ConfirmKeyword'))
    # @removes_context('ConfirmVehicleMakeContext')
    # def handle_confirm_vehicle_make_intent(self, message):
    #     user_confirm = message.data.get('ConfirmKeyword')
    #     self.speak("You said: {}".format(user_confirm))
    #     if user_confirm == 'yes':
    #         self.search_query.update('make', )

    def stop(self):
        pass


def create_skill():
    return OBD2CodesSkill()
