---
title: ctgov
namespace: ctgov
description: ctgov(ClinicalTrials.gov) aggregates information about clinical trials from ClinicalTrials.gov
dependencies: 
  - name: ctgov
    url: https://aact.ctti-clinicaltrials.org/pipe_files
---

## Description
 - This directory contains data obtained from ClinicalTrials.gov. 
 - The data is stored in parquet format. Descriptions for columns for each of the ctgov data tables are listed below. Each data table has unique column names. 
 - The data was obtained from the following link https://aact.ctti-clinicaltrials.org/pipe_files
 
### Data Table List
  - active_storage_attachments.parquet
  - active_storage_biobs.parquet
  - baseline_counts.parquet
  - baseline_measurements.parquet
  - brief_summaries.parquet
  - browse_conditions.parquet
  - browse_interventions.parquet
  - calculated_values.parquet
  - central_contacts.parquet
  - conditions.parquet
  - countries.parquet
  - design_groups_interventions.parquet
  - design_groups.parquet
  - design_outcomes.parquet
  - designs.parquet
  - detailed_descriptions.parquet
  - documents.parquet
  - drop_withdrawals.parquet
  - eligibilities.parquet
  - facilities.parquet
  - facility_contacts.parquet
  - facility_investigators.parquet
  - file_records.parquet
  - id_information.parquet
  - intervention_other_names.parquet
  - interventions.parquet
  - ipd_information_types.parquet
  - keyword.parquet
  - links.parquet
  - milestones.parquet
  - outcome_analyses.parquet
  - outcome_analysis_groups.parquet
  - outcome_counts.parquet
  - outcome_measurement.parquet
  - outcomes.parquet
  - overall_officals.parquet
  - participant_flows.parquet
  - pending_results.parquet
  - provided_documents.parquet
  - reported_event_totals.parquet
  - reported_events.parquet
  - responsible_parties.parquet
  - result_agreements.parquet
  - result_contacts.parquet
  - result_groups.parquet
  - search_results.parquet
  - sponsors.parquet
  - studies.parquet
  - study_references.parquet

### Universal Columns
  - id: Internal database identifcation number
  - nct_id: National Clinical Trials identification number
All files have these two columns except for active_storage_attachments and active_storage_blobs which only have id

### active_storage_attachments
  - name: name of the record
  - record_type: the type of record
  - record_id: id for the record the file is attached to
  - blob_id: id of the attachedment
  - created_at: time created at
### active_storage_blobs
  - id: blob_id
  - key: key for the storage file
  - filename: name of the file
  - content_type: type of file 
  - metadata: metadata for the file
  - byte_size: size of file
  - checksum: value that represents the number of bits
  - created_at: time created at
### baseline_counts
  - result_group_id: id of the result group
  - ctgov_group_code: group code given by ctgov
  - units: The unit of the study e.g. participants, implants
  - scope: scope of which units are included in the count e.g. overall
  - count: number of units
### baseline_measurements
  - result_group_id: id of the result group
  - ctgov_group_code: group code given by ctgov
  - classification: classification of measurement
  - category: category of measurement
  - title: title of measurement
  - description: further description of measurement
  - units: units of the measurement
  - param_type: the type of measurement taken e.g. mean, number, etc.
  - param_value: value of measurement
  - param_value_num: numeric value of measurement
  - dispersion_type: the type of measurement used to evaluate dispersion of param_value e.g. standard deviation
  - dispersion_value: value of dispersion
  - dispersion_value_num: numeric value of dispersion
  - dispersion_lower_limit: lower limit of dispersion
  - dispersion_upper_limit: upper limit of dispersion
  - explanation_of_na: explanation of why a unit is not used
### brief_summaries
  - description: brief summary of the study
### browse_conditions
  - mesh_term: condition which the study falls under
  - downcase_mesh_term: lowercase of the condition
  - mesh_type: mesh type
### browse_interventions
  - mesh_term: intervention which the study falls under
  - downcase_mesh_term: lowercase of intervention
  - mesh_type: mesh type
### calculated_values
  - number_of_facilities: number of facilities used in the study
  - number_of_nsae_subjects: number of subjects with non-serious adverse events
  - number_of_sae_subjects: number of subjects with serious adverse events
  - registered_in_calendar_year: when the clinical trial was registered
  - nlm_download_date: download date of nlm
  - actual_duration: duration of the study
  - were_results_reported: True/False value of whether the results of the study were reported
  - months_to_report_results: months the study has left to report their results
  - has_us_facility: True/False value of whether the facility was in the US
  - has_single_facility: True/False value of whether the study has one facility
  - minimum_age_num: minimum age of eligibility
  - maximum_age_num: maximum age of eligibility
  - number_of_secondary_outcomes_to_measure: number of secondary outcomes in the study
  - number_of_other_outcomes_to_measure: number of other outcomes of the study
### central_contacts
  - contact_type: type of contact for the study e.g. primary/backup
  - name: name of the contact
  - phone: contact phone number
  - email: contact email
### conditions
  - name: name of the condition studied
  - downcase_name: lowercase name of condition
### countries
  - name: country name
  - removed: True/False value of whether the country name was removed
### design_group_interventions
  - design_group_id: ID for design group within study
  - intervention_id: ID for intervention group within study
### design_groups
  - group_type: type of experimental group e.g. experimental, placebo
  - title: title of group
  - description: description of the group
### design_outcomes
  - outcome_type: type of outcome e.g. primary, secondary, etc.
  - measure: how the outcome is measured
  - time_frame: time frame in which the outcome is measured
  - population: target population of the study
  - description: description of the outcome
### designs
  - allocation: How the study groups were assigned e.g. randomized, non-randomized, etc.
  - intervention_model: type of intervention used e.g single-group, parallel assignment, factorial assignment, etc.
  - observational_model: type of observational study if the study was observational in nature
  - primary_purpose: purpose of study e.g. treatment, prevention, etc.
  - time_perspective: time period of the study
  - masking: type of blind study was performed e.g. single-blind, double-blind, open label, etc.
  - masking_description: description of the blinding process of the study
  - intervention_model_description: description of the intervention
  - subject_masked: True/False value for if the subject was blinded to what intervention they were receiving
  - caregiver_masked: True/False value for if the caregiver was blinded to what intervention the subject was receiving
  - investigator_masked: True/False value for if the investigator was blinded to what intervention the subject was receiving
  - outcome_assessor_masked: True/False value for if the outcome assessor was blinded to what intervention the subject was receiving
### detailed_description
  - description: detailed description of the study
### documents
  - document_id: ID of attached document to clinical trial
  - document_type: type of document 
  - url: url to the document
  - comment: comment about document
### drop_withdrawals
  - result_group_id: ID of result group
  - ctgov_group_code: code given to group by ctgov
  - period: part of the study subject(s) withdrew from
  - reason: reason for withdrawal
  - count: number of withdrawals
### eligibilities
  - sampling_method: method which participants were chosen
  - gender: gender(s) selected for participation
  - minimum_age: minimum age for study eligibility
  - maximum_age: maximum age for study eligibility
  - healthy_volunteers: True/False value for whether the study only recruited healthy subjects
  - population: target population of study
  - criteria: inclusion and exclusion criteria for study eligibility
  - gender_description: description of gender selected
  - gender_based: how gender factored into the study
### facilities
  - status: status of the study e.g. recruiting, completed, etc.
  - name: name of facility
  - city: city of facility
  - state: state of facility
  - zip: zip code of facility
  - country: country of facility
### facility_contacts
  - facility_id: ID for facility
  - contact_type: type of contact for the study e.g. primary/backup
  - name: name of contact
  - email: contact email
  - phone: contact phone number
### facility_investigators
  - facility_id: ID for facility
  - role: role of facility investigator in the study
  - name: name of investigator
### file_records
  - filename: name of the file
  - file_size: size of the file
  - file_type: type of file
  - created_at: date file was created
  - updated_at: date file was last updated
  - url: url of the file
### id_information
  - id_type: type of id
  - id_value: value id corresponds to
### intervention_other_names
  - intervention_id: id of intervention
  - name: alternate name of intervention used in clinical trial
### interventions
  - intervention_type: type of intervention
  - name: name of intervention
  - description: description of intervention
### ipd_information_types
  - name: name of ipd information type
### keywords
  - name: name of keyword of clincial trial
  - downcase_name: lowercase of keyword
### links
  - url: link associated with clincal trial
  - description: description of link
### milestones
  - result_group_id: id of the result group
  - ctgov_group_code: group code given by ctgov
  - title: milestone the study has passed e.g. started, completed, etc.
  - period: the period of the study the milestone is referring to e.g. overall study, treatment, etc.
  - description: description of milestone
  - count: number of subjects in the study
### outcome_analyses
  - outcome_id: id of outcome for the clinical trial
  - non-inferiority_type: type of non-inferiority
  - non_inferiority_description: description of non-inferiority
  - param_type: parameter which the outcome was measured in
  - param_value: value of the outcome parameter
  - dispersion_type: type of dispersion measurement used to evaluate the outcome
  - dispersion_value: value of the dispersion measurement
  - p_value_modifier: modifier of the p-value
  - p_value: value of the p-value
  - ci_n_sides: number of sides for the confidence interval 
  - ci_percent: percentage value of the confidence interval e.g. 95%
  - ci_lower_limit: lower limit of the confidence interval
  - ci_upper_limit: upper limit of the confidence interval
  - p_value_description: description of p-value
  - method: method for generating p-value e.g. ANOVA
  - method_description: description of method
  - estimate_description: description of estimate
  - groups_description: description of groups used in statistical analysis
  - other_analysis_description: description of other statistical analyses used
### outcome_analysis_id
  - outcome_analysis_id: id of outcome analysis
  - result_group_id: id of the result group
  - ctgov_group_code: group code given by ctgov
### outcome_counts
  - result_group_id: id of the result group
  - ctgov_group_code: group code given by ctgov
  - scope: scope of which units are included in the count e.g. overall
  - units: The unit of the study e.g. participants, implants
  - count: number of units
### outcome_measurements
  - result_group_id: id of the result group
  - ctgov_group_code: group code given by ctgov
  - classification: classification of measurement
  - category: category of measurement
  - title: title of measurement
  - description: further description of measurement
  - units: units of the measurement
  - param_type: the type of measurement taken e.g. mean, number, etc.
  - param_value: value of measurement
  - param_value_num: numeric value of measurement
  - dispersion_type: the type of measurement used to evaluate dispersion of param_value e.g. standard deviation
  - dispersion_value: value of dispersion
  - dispersion_value_num: numeric value of dispersion
  - dispersion_lower_limit: lower limit of dispersion
  - dispersion_upper_limit: upper limit of dispersion
  - explanation_of_na: explanation of why a unit is not used
### outcomes
  - outcome_type: type of outcome
  - title: title of outcome
  - description: description of outcome
  - time_frame: time frame which the outcome was evaluated
  - population: target population of the study
  - anticipated_posting_date: 
  - anticipated_posting_month_year
  - units: units of outcome
  - units_analyzed: how the unit was analyzed
  - dispersion_type: the type of measurement used to evaluate dispersion of param_value e.g. standard deviation
  - param_type: the type of measurement taken e.g. mean, number, etc.
### overall_officials
  - role: role of study official
  - name: name of study official
  - affiliation: affiliation of the study official
### participant_flows
  - recruitment_details: explanation of how participants were recruited
  - pre_assignment_details: description of how participants were separated into groups
### pending_results
  - event: event of the trial
  - event_date_description: date of event in format of month_name, day, year
  - event_date: date of event in format of year-month-day
### provided_documents
  - document_type: type of document provided
  - has_protocol: True/False value for whether trial has protocol
  - has_icf: True/False value for whether trial has icf
  - has_sap: True/False value for whether trial has sap
  - document_date: date document was provided
  - url: url of document
### reported_events_total
  - ctgov_group_code: group code given by ctgov
  - event_type: type of adverse event e.g. serious, other, death, etc.
  - classification: classification of adverse event e.g. total, serios adverse events, other adverse events
  - subjects_affected: number of subjects affected
  - subjects_at_risk: number of subjects at risk of adverse event
  - created_at: date event was created
  - updated_at: date event was updated
### reported_events
  - ctgov_group_code: group code given by ctgov
  - time_frame: time frame which adverse event occured
  - event_type: type of event
  - default_vocab: default medical dictionary vocab used to refer to the event
  - default_assessment: default assessment of the event
  - subjects_affected: number of subjects affected
  - subject_at_risk: number of subjects at risk of adverse event
  - description: description of the adverse event
  - event_count: number of events
  - organ_system: organ system the event is affecting
  - adverse_event_term: term for event
  - frequency_threshold: number scale for how frequent the event is
  - vocab: medical dictionary used for assessment of event e.g. MedDRA
  - assessment: type of assessment of event
### responsible_parties
  - responsible_party_type: type of responsible party e.g. sponser, principal investigator
  - name: name of responsible party
  - title: title of responsible party e.g. PhD, MD
  - organization: organization of responsible party
  - affiliation: institution of responsible party
### result_agreements
  - pi_employee: y/n value for if the signee of agreement is an employee of the PI
  - agreement: agreement description
  - restriction_type: type of restriction agreement
  - other_details: whether other details are in the agreement either blank or OTHER
  - restrictive_agreement: wording of the agreement
### result_contacts
  - organization: organization of contact
  - name: name of contact
  - phone: contact number
  - email: contact email
  - extension: extenesion for phone number
### result_groups
  - ctgov_group_code: group code given by ctgov
  - result_type: type of result group
  - title: title of result group
  - description: description of result group
### search_results
  - name: name of search result
  - created_at: date created
  - updated_at: date updated
  - grouping: grouping which search results belong to
  - study_search_id: id for study search
### sponsors
  - agency_class: class the sponsor agency belongs to e.g. industry, other, etc.
  - lead_or_collaborator: lead or collaborator on study
  - name: name of sponsor
### studies
  - nlm_download_date_description: description of nlm download date
  - study_first_submitted_date: date when the study was first submitted
  - results_first_submitted_date: date when resultes were first submitted
  - disposition_first_submitted_date: date when disposition was first submitted
  - last_update_submitted_date: date of last update
  - study_first_submitted_qc_date: qc type of date of when the study was first submitted
  - study_first_posted_date: date of when the study was first posted
  - study_first_posted_data_type: type of date of when the study was first posted
  - results_first_submitted_qc_date: qc date of when the results was first submitted
  - results_first_posted_date: date of when the results was first posted
  - results_first_posted_date_type: type of date of when the results was first posted
  - disposition_first_submitted_qc_date: qc date of when the disposition were first submitted
  - disposition_first_posted_date: date of when the disposition was first posted
  - disposition_first_posted_date_type: type of date of when the disposition was first posted
  - last_update_submitted_qc_date: qc date of the last updated posted
  - last_update_posted_date: date of the last update posted
  - last_update_posted_date_type: type of date of the last update posted
  - start_month_year: month/year of the study start
  - start_date_type: type of date of the study start
  - start_date: date of the study start
  - verification_month_year: month/year of verification
  - verification_date: date of verification
  - completion_month_year: month/year of completion
  - completion_date_type: type of date of completion
  - completion_date: date of completion
  - primary_completion_month_year: month/year of primary completion
  - primary_completion_date_type: type of date of primary completion
  - primary_completion_date: date of primary completion
  - target_duration: how long the study is planned to be
  - study_type: type of study e.g. interventional, observational, etc.
  - acronymn: acronumn used for the study
  - baseline_population: baseline population for the study
  - brief_title: short title of the study
  - ofiicial_title: formal title of the study
  - overall_status: overall status of the study e.g. completed, recruiting, etc.
  - last_known_status: last known status of the study e.g. completed, recruiting, etc.
  - phase: phase which the study is in
  - enrollment: number of enrolled
  - enrollment_type: type of enrollment used for the study
  - source: where the enrollments are coming from
  - limitation_and_caveats: limitations/caveats of the study
  - number_of_arms: number of arms in the study
  - number_of_groups: number of groups in the study
  - why_stopped: reason why the study was stopped
  - has_expanded_access: True/False value for whether study has expanded access
  - expanded_access_type_individual: type of expanded access for individuals
  - expanded_access_type_intermediate: type of expanded access for intermediates
  - expanded_access_type_treatment: type of expanded access treatment
  - has_dmc: True/False value for whether the study has dmc
  - is_fda_regulated_drug: True/False value for whether the drug in the study is an fda regulated drug
  - is_fda_regulated_device: True/False value for whether the device in the study is an fda regulated device
  - is_unapproved_device: True/False value for whether there is an unapproved device in the study
  - is_ppsd: True/False value for whether there is ppsd
  - is_us_export: True/False value for whether device is an us export
  - biospec_retention: True/False value for biospecimen will be kept
  - biospec_description: description of biospecimen 
  - ipd_time_frame: time frame of ipd
  - ipd_access_criteria: access criteria for ipd
  - ipd_url: url for ipd
  - plan_to_share_ipd: True/False value for whether there is a plan to share ipd
  - plan_to_share_ipd_description: descriptin of plans to share ipd
  - created_at: date of creation of study status
  - updated_at: date of update to study status
### study_references
  - pmid: pmid of reference
  - reference_type: type of reference e.g. background, result, etc.
  - citation: citation of reference
  




## Data Retrieval
* Data on the ftp website are updated on a daily basis. 
https://aact.ctti-clinicaltrials.org/pipe_files

### Data stored in Parquet files
* Data can be downloaded using the following commands. To retrieve the data, make sure that dvc is downloaded

**Retrieving a single file**
```
dvc get git@github.com:insilica/oncindex-bricks.git bricks/ctgov/data/outcomes.parquet -o data/outcomes.parquet
```
**It is advised to import files into a project so that you will be able to track changes in the data set**
```
dvc import git@github.com:insilica/oncindex-bricks.git bricks/ctgov/data -o data
```
