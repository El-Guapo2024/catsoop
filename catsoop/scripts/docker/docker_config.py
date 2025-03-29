# Docker-optimized CAT-SOOP configuration
# This file contains settings optimized for running CAT-SOOP in a Docker container

import os

# Authentication
cs_auth_type = "dummy"
cs_auth_dummy_username = "default_user"
cs_auth_dummy_password = "default_password"

# Logging
cs_logging_level = "INFO"
cs_logging_dir = "/catsoop/data/logs"

# Server Configuration
cs_url_root = "http://localhost:7667"
cs_host = "0.0.0.0"
cs_port = 7667

# Set default course
cs_default_course = "number_sense"

# Course Settings
cs_courses = {
    "number_sense": {
        "name": "Number Sense",
        "instructor": "default_user",
        "institution": "CAT-SOOP Docker Demo",
        "contact_email": "admin@example.com",
        "markup_language": "md",
        "description": "Number Sense Course",
        "allow_paste": True,
        "default_language": "python",
        "course_contact_email": "admin@example.com",
        "course_contact_name": "Admin User",
        "course_home_path": ["__HANDLERS__", "default", "home"],
        "course_name": "Number Sense",
        "course_number": "NS101",
        "course_title": "Number Sense Course",
        "default_language": "python",
        "display_question_names": True,
        "display_question_numbers": True,
        "display_threshold": 0.5,
        "force_local": False,
        "ignore_submission_field": False,
        "ignore_submission_field_if_not_found": False,
        "institution": "CAT-SOOP Docker Demo",
        "instructor": "default_user",
        "markup_language": "md",
        "name": "Number Sense",
        "num_questions": 0,
        "num_questions_to_display": 0,
        "question_name_prefix": "Q",
        "question_number_prefix": "Q",
        "question_number_style": "decimal",
        "question_number_threshold": 0.5,
        "question_prefix": "Q",
        "question_prefix_if_not_found": False,
        "question_prefix_if_not_found_style": "decimal",
        "question_prefix_if_not_found_threshold": 0.5,
        "question_prefix_style": "decimal",
        "question_prefix_threshold": 0.5,
        "question_threshold": 0.5,
        "questions": {},
        "score_based_on": "best",
        "show_instructor_names": True,
        "show_question_names": True,
        "show_question_numbers": True,
        "show_student_names": True,
        "show_threshold": 0.5,
        "student": "default_user",
        "student_names": {},
        "student_photos": {},
        "student_username": "default_user",
        "submit_button_text": "Submit",
        "submit_button_text_if_not_found": "Submit",
        "submit_button_text_if_not_found_style": "decimal",
        "submit_button_text_if_not_found_threshold": 0.5,
        "submit_button_text_style": "decimal",
        "submit_button_text_threshold": 0.5,
        "submit_text": "Submit",
        "submit_text_if_not_found": "Submit",
        "submit_text_if_not_found_style": "decimal",
        "submit_text_if_not_found_threshold": 0.5,
        "submit_text_style": "decimal",
        "submit_text_threshold": 0.5,
        "submission_button_text": "Submit",
        "submission_button_text_if_not_found": "Submit",
        "submission_button_text_if_not_found_style": "decimal",
        "submission_button_text_if_not_found_threshold": 0.5,
        "submission_button_text_style": "decimal",
        "submission_button_text_threshold": 0.5,
        "submission_text": "Submit",
        "submission_text_if_not_found": "Submit",
        "submission_text_if_not_found_style": "decimal",
        "submission_text_if_not_found_threshold": 0.5,
        "submission_text_style": "decimal",
        "submission_text_threshold": 0.5,
        "threshold": 0.5,
        "total_points": 0,
        "total_questions": 0,
        "total_questions_to_display": 0,
        "total_threshold": 0.5,
        "username": "default_user",
    }
}

# Security
cs_secret_key = "docker_secret_key_please_change_in_production"
cs_encryption_key = "docker_encryption_key_please_change_in_production"

# Debug Level
cs_debug_level = 0

# Filesystem Configuration
cs_fs_root = "/catsoop/catsoop"  # This should point to the CAT-SOOP source code directory
cs_data_root = "/catsoop/data"   # This should point to the data directory

# Additional Settings
cs_wsgi_server = "waitress"
cs_wsgi_server_log_level = "INFO"
cs_wsgi_server_max_request_body_size = 33554432  # 32MB
cs_wsgi_server_channel_timeout = 300
cs_wsgi_server_connection_limit = 1000
cs_wsgi_server_threads = 4 