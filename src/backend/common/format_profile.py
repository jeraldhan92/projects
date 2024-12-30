def format_profile_message(profile):
    human_message = ""
    if profile.name is not None:
        human_message += f"My name is {profile.name}. "
    if profile.age is not None:
        human_message += f"I am {profile.age} years old. "
    human_message += (
        f"I am an {profile.employment_status} in the {profile.industry} industry. "
    )
    if profile.occupation is not None:
        human_message += f"My job title is {profile.occupation}. "
    return human_message


if __name__ == "__main__":

    class Profile:
        name = "Mary"
        age = 25
        employment_status = "Employer"
        occupation = "Software Engineer"
        industry = "Tech"

    print(format_profile_message(Profile()))
