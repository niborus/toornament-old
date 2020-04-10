scopes = [
#Usage:         Name of the scope         Getting an Token     Describtion
    [
        "participant:manage_registrations",     False   #Grants the ability to manage the registrations of a user.
    ], [
        "participant:manage_participations",    False   #Grants the ability to manage the participations of a user.
    ], [
        "user:info",                            True    #Grants access to public user information.
    ], [
        "organizer:view",                       True    #Grants the ability to list tournaments and see their settings.
    ], [
        "organizer:admin",                      False   #Grants the ability to create a tournament and edit its settings.
    ], [
        "organizer:result",                     True   #Grants the ability to edit match information and referee results.
    ], [
        "organizer:participant",                True    #Grants the ability to manage the participants of a tournament.
    ], [
        "organizer:registration",               True    #Grants the ability to manage the registrations of a tournament.
    ], [
        "organizer:permission",                 False   #Grants the ability to manage the permissions of a tournament.
    ], [
        "organizer:delete",                     False   #Grants the ability to delete tournaments.
    ]
]
