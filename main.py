import pandas as pd
from nslookup import Nslookup
import dns.reversename


def generate_test_data(domain_list):
    # Function to perform DNS lookup for each domain
    def get_nslookup(domain, verbose=False, tcp=False):
        dns_query = Nslookup()
        ips_record = dns_query.dns_lookup(domain)
        return ips_record.answer

    def ger_reverse_lookup(ips_record):
        return dns.reversename.from_address(ips_record)

    data = []
    for domain in domain_list:
        get_ip_address_from_domain = get_nslookup(domain.get("domain"))
        get_reverse_domain_from_ip = ger_reverse_lookup(domain.get("ip_address"))
        data.append(
            {"domain": domain.get("domain"),
             "ip_address": domain.get("ip_address"),
             "ip_address_from_domain": get_ip_address_from_domain[0],
             "reverse_domain_from_ip": get_reverse_domain_from_ip})

    # Creating a DataFrame using pandas
    df = pd.DataFrame(data)

    return df


if __name__ == '__main__':
    domain_list = pd.read_csv("test_data.csv").to_dict(orient="records")
    result_frame = generate_test_data(domain_list)
    result_frame.to_csv("test_csv_file.csv")
