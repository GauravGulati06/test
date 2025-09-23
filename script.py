def extract_emails_from_str(text: str) -> list:
    """_summary_
    args: 
        - str (emails separated by space & saved into a list)
    process:
        - find the email indexes in the list
        - search by single `@` symbol followed by a `.` symbol 
        - sequence of characters matters
        - save those emails into a list, discarding remaining indexes (i.e. strings without `@` or `.`)
    return:
        - return the list of emails
    """
    emails = []
    print(f"Words: {text.split()}")
    
    for word in text.split():
    # Check for exactly one '@' and at least one '.' after '@'
        if word.count('@') == 1:
            local, domain = word.split('@')
            if '.' in domain and local and domain.split('.', 1)[0]:
                emails.append(word)

    return (f"Emails: {emails}")

def write_initials(text: str) -> str:
    """Extracts initials from a given string.
    args: 
        - str (full name or phrase), e.g. "mahindra singh dhoni"
    process:
        - split the string into a list of words
        - take the last word as the surname
        - take the first letter of each of the other words as initials
        - concatenate the initials and surname with dots in between
    return:
        - return the initials as a string, e.g. "M.S. Dhoni"
    """

    words = text.strip().split()
    if not words:
        return ""
    print(f"Words: {words}")
    
    surname = words[-1].capitalize()
    initials = ".".join([w[0].upper() for w in words[:-1]]) + "."
    
    return (f"Initials: {initials} {surname}")


if __name__ == "__main__":
    print("Email Extraction:")
    print(extract_emails_from_str("Contact us at support@company.com or info@company.com and look for more info at AK.@@company.com"))
    
    print("\nInitials Extraction:")
    print(write_initials("mahindra singh dhoni"))
