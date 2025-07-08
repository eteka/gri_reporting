# org_info_collector.py
# Collects key information based on GRI 2-1 disclosures
def collect_organizational_details():
    print("\n📋 GRI 2-1: Organizational Details\n(Enter your responses. Type 'skip' to leave blank)\n")
    org_data = {}
    org_data["legal_name"] = input("1. Legal name: ")
    org_data["business_name"] = input("2. Trade/business name (if different): ")
    org_data["ownership_type"] = input("3. Ownership type (public, private, NGO…): ")
    org_data["legal_form"] = input("4. Legal form (Ltd, PLC, Inc…): ")
    org_data["headquarters_location"] = input("5. Headquarters (City, Country): ")
    org_data["countries_of_operation"] = input("6. Countries of operation (comma-separated): ")
    return org_data

def display_summary(data):
    print("\n✅ Summary:")
    for k, v in data.items():
        label = k.replace('_', ' ').title()
        print(f"- {label}: {v if v else '[Not provided]'}")
    print()

if __name__ == "__main__":
    info = collect_organizational_details()
    display_summary(info)
