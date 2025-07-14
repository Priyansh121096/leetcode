# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            try:
                plus_idx = local.index('+')
                local = local[:plus_idx]
            except ValueError:
                pass
                
            local = local.replace('.', '')
            actual_email = f"{local}@{domain}"
            seen.add(actual_email)

        return len(seen)
