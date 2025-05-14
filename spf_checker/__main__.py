import dns.resolver
import spf

def get_spf_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                decoded = txt_string.decode('utf-8')
                if decoded.startswith('v=spf1'):
                    return decoded
        return None
    except Exception as e:
        return f"DNS lookup failed: {e}"

def validate_spf(domain, spf_record):
    try:
        result = spf.check2(i='127.0.0.1', s=f'test@{domain}', h='mail.' + domain)
        return f"SPF check result: {result[0]} ({result[1]})"
    except Exception as e:
        return f"SPF validation failed: {e}"

def main():
    domain = input("Enter domain name (e.g., example.com): ").strip()
    print(f"\nLooking up SPF record for: {domain}")

    spf_record = get_spf_record(domain)
    if spf_record is None:
        print("No SPF record found.")
    elif spf_record.startswith("DNS lookup failed"):
        print(spf_record)
    else:
        print(f"Found SPF record: {spf_record}")
        validation_result = validate_spf(domain, spf_record)
        print(validation_result)
