class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = {}
        for cpdomain in cpdomains:
            num_idx = cpdomain.index(" ")
            count = int(cpdomain[:num_idx])
            cur = num_idx + 1
            new_domain = cpdomain[cur:]
            domains[new_domain] = domains.get(new_domain, 0) + count
            cp_len = len(cpdomain)
            while cur < cp_len:
                if cpdomain[cur] == ".":
                    cur += 1
                    new_domain = cpdomain[cur:]
                    domains[new_domain] = domains.get(new_domain, 0) + count
                cur += 1
        ans = []
        for domain, count in domains.items():
            ans.append(str(count) + " " + domain)
        return ans