# O(3^(n/4)) time: when rest of string is long enough we try all lengths for block i
# O(1) space: call stack of depth <= 4
def ip_addresses(s, ip_parts=[]):
    addresses = set()

    def buildAddresses(s, prefix, step):
        nonlocal addresses

        if step == 4:
            # valid address
            if s == '': addresses.add(prefix)
            return

        # all of s used, but not built 4 parts yet
        if s == '': return

        if step > 0:
            prefix += '.'

        for i in range(1, 4):
            newBlock = s[:i]
            if int(newBlock) > 255 or len(s) - i < 3 - step: break
            buildAddresses(s[i:], prefix + newBlock, step + 1)
            if newBlock == '0': break

    buildAddresses(s, '', 0)
    return addresses



print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
