# gri_glossary.py

# Simple GRI Glossary Lookup Tool (Based on GRI 1: Foundation 2021)

GRI_GLOSSARY = {
    "impact": (
        "Impact refers to the effect an organization has or could have on the economy, "
        "environment, and people, including on human rights. Impacts may be positive or negative, "
        "actual or potential, and influence sustainable development."
    ),
    "material topic": (
        "Material topics are topics that represent an organization's most significant impacts "
        "on the economy, environment, and people, including human rights. These are prioritized "
        "for reporting."
    ),
    "due diligence": (
        "Due diligence is the process by which an organization identifies, prevents, mitigates, "
        "and accounts for how it addresses actual and potential negative impacts. It includes "
        "remediation where the organization caused or contributed to the impact."
    ),
    "stakeholder": (
        "Stakeholders are individuals or groups with interests that are or could be affected "
        "by the organization’s activities. This includes employees, customers, communities, "
        "suppliers, governments, etc."
    ),
    "accuracy": "Reported information must be sufficiently accurate and detailed to enable evaluation.",
    "balance": "Reports should reflect both positive and negative aspects of performance.",
    "clarity": "Information should be presented in a way that is understandable and accessible.",
    "comparability": "Users should be able to compare information across time and organizations.",
    "completeness": "All significant impacts and related information should be included.",
    "sustainability context": (
        "The report should present the organization's performance in the context of sustainable development."
    ),
    "timeliness": "Reporting should occur on a regular schedule so that information is available in time.",
    "verifiability": "Information should be documented and traceable to support external verification.",
}

def explain_term(term):
    key = term.lower().strip()
    definition = GRI_GLOSSARY.get(key)
    if definition:
        print(f"\n📘 {term.capitalize()}:\n{definition}\n")
    else:
        print(f"\n⚠️ Sorry, no definition found for '{term}'. Try another key concept.\n")

def main():
    print("🧠 Welcome to the GRI Learning Assistant")
    print("Type a GRI concept (e.g., impact, due diligence, clarity) or type 'exit' to quit.\n")

    while True:
        user_input = input("🔍 Enter term: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting GRI Learning Assistant. Goodbye!")
            break
        explain_term(user_input)

if __name__ == "__main__":
    main()

