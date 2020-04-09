import pytz

class abc():

    class tournament():

        class logo():
            def __init__(self, logo_dict):
                self.logo_small = logo_dict.get('logo_small', None)
                self.logo_medium = logo_dict.get('logo_medium', None)
                self.logo_large = logo_dict.get('logo_large', None)
                self.original = logo_dict.get('original', None)

        def __init__(self, tournament_dict):
            self.name = tournament_dict.get('name', None)
            self.full_name = tournament_dict.get('full_name', None)
            self.scheduled_date_start = tournament_dict.get('scheduled_date_start', None)
            self.scheduled_date_end = tournament_dict.get('scheduled_date_end', None)
            self.timezone = tournament_dict.get('timezone', None)
            self.public = tournament_dict.get('public', None)
            self.size = tournament_dict.get('size', None)
            self.online = tournament_dict.get('online', None)
            self.location = tournament_dict.get('location', None)
            self.country = tournament_dict.get('country', None)
            self.logo = tournament_dict.get('logo', None)
            self.registration_enabled = tournament_dict.get('registration_enabled', None)
            self.registration_opening_datetime = tournament_dict.get('registration_opening_datetime', None)
            self.registration_closing_datetime = tournament_dict.get('registration_closing_datetime', None)
            self.organization = tournament_dict.get('organization', None)
            self.contact = tournament_dict.get('contact', None)
            self.discord = tournament_dict.get('discord', None)
            self.website = tournament_dict.get('website', None)
            self.description = tournament_dict.get('description', None)
            self.rules = tournament_dict.get('rules', None)
            self.prize = tournament_dict.get('prize', None)
            self.match_report_enabled = tournament_dict.get('match_report_enabled', None)
            self.registration_request_message = tournament_dict.get('registration_request_message', None)
            self.check_in_enabled = tournament_dict.get('check_in_enabled', None)
            self.check_in_participant_enabled = tournament_dict.get('check_in_participant_enabled', None)
            self.check_in_participant_start_datetime = tournament_dict.get('check_in_participant_start_datetime', None)
            self.check_in_participant_end_datetime = tournament_dict.get('check_in_participant_end_datetime', None)
            self.archived = tournament_dict.get('archived', None)
            self.registration_acceptance_message = tournament_dict.get('registration_acceptance_message', None)
            self.registration_refusal_message = tournament_dict.get('registration_refusal_message', None)
            self.registration_terms_enabled = tournament_dict.get('registration_terms_enabled', None)
            self.registration_terms_url = tournament_dict.get('registration_terms_url', None)
            self.id = tournament_dict.get('id', None)
            self.discipline = tournament_dict.get('discipline', None)
            self.status = tournament_dict.get('status', None)
            self.participant_type = tournament_dict.get('participant_type', None)
            self.platforms = tournament_dict.get('platforms', None)
            self.featured = tournament_dict.get('featured', None)
            self.registration_notification_enabled = tournament_dict.get('registration_notification_enabled', None)
            self.team_min_size = tournament_dict.get('team_min_size', None)
            self.team_max_size = tournament_dict.get('team_max_size', None)

            if tournament_dict.get('logo', None) != None:
                self.logo = abc.tournament.logo(tournament_dict["logo"])


    class participant:
        def __init__(self, participant_dictionary):
            self.custom_fields = participant_dictionary.get('custom_fields', None)
            self.id = participant_dictionary.get('id', None)
            self.name = participant_dictionary.get('name', None)
            self.email = participant_dictionary.get('email', None)
            self.user_id = participant_dictionary.get('user_id', None)
            self.custom_user_identifier = participant_dictionary.get('custom_user_identifier', None)
            self.checked_in = participant_dictionary.get('checked_in', None)
            self.checked_in_at = participant_dictionary.get('checked_in_at', None)
            self.created_at = participant_dictionary.get('created_at', None)

    class opponent:
        def __init__(self, opponent_dictionary):
            self.number = opponent_dictionary.get('number', None)
            self.position = opponent_dictionary.get('position', None)

            self.rank = opponent_dictionary.get('rank', None)
            self.result = opponent_dictionary.get('result', None)
            self.forfeit = opponent_dictionary.get('forfeit', None)
            self.score = opponent_dictionary.get('score', None)

            if opponent_dictionary.get('participant', None) == None:
                self.participant = None
            else:
                self.participant = abc.participant(opponent_dictionary['participant'])

    class match:
        def __init__(self, match_dictionary):
            self.id = match_dictionary.get('id', None)
            self.stage_id = match_dictionary.get('stage_id', None)
            self.group_id = match_dictionary.get('group_id', None)
            self.round_id = match_dictionary.get('round_id', None)
            self.number = match_dictionary.get('number', None)
            self.type = match_dictionary.get('type', None)
            self.status = match_dictionary.get('status', None)
            self.settings = match_dictionary.get('settings', None)

            self.public_note = match_dictionary.get('public_note', None)
            self.private_note = match_dictionary.get('private_note', None)
            self.report_closed = match_dictionary.get('report_closed', None)
            self.opponents = []

            if match_dictionary.get('scheduled_datetime', None) == None:
                self.scheduled_datetime = None
            else:
                self.scheduled_datetime = own.convertdatetime(match_dictionary.get('scheduled_datetime')).astimezone(
                    pytz.timezone('Europe/Berlin'))

            if match_dictionary.get('played_at', None) == None:
                self.played_at = None
            else:
                self.played_at = own.convertdatetime(match_dictionary.get('played_at')).astimezone(
                    pytz.timezone('Europe/Berlin'))

            for i in match_dictionary.get('opponents', []):
                k = abc.opponent(i)
                self.opponents.append(k)

    class round:
        def __init__(self, dictionary):
            self.id = dictionary.get('id', None)
            self.group_id = dictionary.get('group_id', None)
            self.stage_id = dictionary.get('stage_id', None)
            self.number = dictionary.get('number', None)
            self.name = dictionary.get('name', None)
            self.closed = dictionary.get('closed', None)
            self.settings = dictionary.get('settings', None)

    class group:
        def __init__(self, dictionary):
            self.id = dictionary.get('id', None)
            self.stage_id = dictionary.get('stage_id', None)
            self.number = dictionary.get('number', None)
            self.name = dictionary.get('name', None)
            self.closed = dictionary.get('closed', None)
            self.settings = dictionary.get('settings', None)

    class stage:
        def __init__(self, dictionary):
            self.id = dictionary.get('id', None)
            self.number = dictionary.get('number', None)
            self.name = dictionary.get('name', None)
            self.type = dictionary.get('type', None)
            self.closed = dictionary.get('closed', None)
            self.settings = dictionary.get('settings', None)