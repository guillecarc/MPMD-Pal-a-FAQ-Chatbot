## story_15: scholarships
* master_scholarships
    - utter_master_scholarships   <!-- predicted: utter_master_degree -->


## story_16: semester_content
* master_semester_content
    - utter_master_semester_one_subjects   <!-- predicted: utter_master_program_content -->
    - utter_master_semester_three_subjects   <!-- predicted: action_listen -->
    - utter_master_semester_two_subjects   <!-- predicted: action_listen -->


## story_17: starting_date
* master_start
    - utter_master_start   <!-- predicted: utter_master_degree -->


## story_18: tuition_fees
* master_tuition_fees
    - utter_master_tuition_fees   <!-- predicted: utter_master_degree -->


## story_21: greet + tuition_fees + scholarship + thank + good_deny + bye
* greet
    - utter_greet
* master_tuition_fees
    - utter_master_tuition_fees   <!-- predicted: utter_greet -->
* master_scholarships
    - utter_master_scholarships   <!-- predicted: utter_greet -->
* thank
    - utter_thank
* good_deny
    - utter_bye


## story_24: starting_date + semester_content + thank + good_deny + bye
* master_start
    - utter_master_start   <!-- predicted: utter_master_degree -->
* master_semester_content
    - utter_master_semester_one_subjects   <!-- predicted: utter_master_program_content -->
    - utter_master_semester_three_subjects   <!-- predicted: action_listen -->
    - utter_master_semester_two_subjects   <!-- predicted: action_listen -->
* thank
    - utter_thank
* good_deny
    - utter_bye


## story_25: program_content + further_qualification + career_opportunities + semester_content + electives
* master_program_content
    - utter_master_program_content
* master_further_qualification_opportunities
    - utter_master_further_qualification_opportunities
* master_career_opportunities
    - utter_master_career_opportunities
* master_semester_content
    - utter_master_semester_one_subjects   <!-- predicted: utter_master_program_content -->
    - utter_master_semester_three_subjects   <!-- predicted: action_listen -->
    - utter_master_semester_two_subjects   <!-- predicted: action_listen -->
* master_electives
    - utter_master_electives   <!-- predicted: action_deactivate_form -->


## story_26: tuition_fees + scholarships + starting_date + bye
* master_tuition_fees
    - utter_master_tuition_fees   <!-- predicted: utter_master_degree -->
* master_scholarships
    - utter_master_scholarships   <!-- predicted: utter_master_program_content -->
* master_start
    - utter_master_start   <!-- predicted: utter_master_program_content -->
* bye
    - utter_bye


## story_29: greet + program_content + semester_content + electives + start
* greet
    - utter_greet
* master_program_content
    - utter_master_program_content
* master_semester_content
    - utter_master_semester_one_subjects   <!-- predicted: utter_master_program_content -->
    - utter_master_semester_three_subjects   <!-- predicted: action_listen -->
    - utter_master_semester_two_subjects   <!-- predicted: action_listen -->
* master_electives
    - utter_master_electives   <!-- predicted: utter_master_semester_three_subjects -->
* master_start
    - utter_master_start   <!-- predicted: utter_master_program_content -->


## story_9: electives
* master_electives
    - utter_master_electives   <!-- predicted: utter_master_degree -->


