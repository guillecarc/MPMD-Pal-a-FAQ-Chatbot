# FAQ actions to exclude the questions from the tracker and force a follow up action to "action_listen"

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import *

# =============================================================================
# bye
# =============================================================================
class bye(Action):
  
  def name(self):
    return "action_bye"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_bye", tracker)
    return [UserUtteranceReverted()]

# =============================================================================
# greet    
# =============================================================================
class greet(Action):
  
  def name(self):
    return "action_greet"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_greet", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]
    
# =============================================================================
# master_admission_requirements
# =============================================================================
class master_admission_requirements(Action):
  
  def name(self):
    return "action_master_admission_requirements"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_admission_requirements", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_application_period
# =============================================================================
class master_application_period(Action):
  
  def name(self):
    return "action_master_application_period"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_application_period", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_career_opportunities
# =============================================================================
class master_career_opportunities(Action):
  
  def name(self):
    return "action_master_career_opportunities"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_career_opportunities", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_contact
# =============================================================================
class master_contact(Action):
  
  def name(self):
    return "action_master_contact"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_contact", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_degree
# =============================================================================
class master_degree(Action):
  
  def name(self):
    return "action_master_degree"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_degree", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_duration
# =============================================================================
class master_duration(Action):
  
  def name(self):
    return "action_master_duration"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_duration", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_electives
# =============================================================================
class master_electives(Action):
  
  def name(self):
    return "action_master_electives"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_electives", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_further_qualification_opportunities
# =============================================================================
class master_further_qualification_opportunities(Action):
  
  def name(self):
    return "action_master_further_qualification_opportunities"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_further_qualification_opportunities", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_how_to_apply
# =============================================================================
class master_how_to_apply(Action):
  
  def name(self):
    return "action_master_how_to_apply"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_how_to_apply", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_language
# =============================================================================
class master_language(Action):
  
  def name(self):
    return "action_master_language"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_language", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_location
# =============================================================================
class master_location(Action):
  
  def name(self):
    return "action_master_location"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_location", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_program_content
# =============================================================================
class master_program_content(Action):
  
  def name(self):
    return "action_master_program_content"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_program_content", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_master_scholarships
# =============================================================================
class master_scholarships(Action):
  
  def name(self):
    return "action_master_scholarships"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_scholarships", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# master_semester_content
# =============================================================================
class master_semester_content(Action):
  
  def name(self):
    return "action_master_semester_content"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_semester_one_subjects", tracker)
    dispatcher.utter_template("utter_master_semester_two_subjects", tracker)
    dispatcher.utter_template("utter_master_semester_three_subjects", tracker)
    return [UserUtteranceReverted(),
            UserUtteranceReverted(),
            UserUtteranceReverted(),
            FollowupAction("action_listen")]


# =============================================================================
# master_start
# =============================================================================
class master_start(Action):
  
  def name(self):
    return "action_master_start"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_start", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]


# =============================================================================
# master_tuition_fees
# =============================================================================
class master_tuition_fees(Action):
  
  def name(self):
    return "action_master_tuition_fees"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_master_tuition_fees", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]

# =============================================================================
# thank
# =============================================================================
class thank(Action):
  
  def name(self):
    return "action_thank"
    
  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_thank", tracker)
    return [UserUtteranceReverted(),FollowupAction("action_listen")]








