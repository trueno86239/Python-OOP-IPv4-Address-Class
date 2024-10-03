class NetIPv4:

    def __init__(self, ip):
        self.ip = str(ip)
        self.octets = self.split_ip()

    def split_ip(self):
        return self.ip.split(".")

    def is_valid(self):
        if len(self.octets) != 4:
            return False
        for x in self.octets:
            try:
                if int(x) < 0 or int(x) > 255:
                    return False
            except ValueError:
                return False
        return True

    def get_as_string(self):
        return self.ip
    
    def get_as_int(self):
        octets = list(map(int, self.octets))
        int_ip = (16777216 * octets[0]) + (65536 * octets[1]) + (256 * octets[2]) + octets[3]
        return int_ip

    def get_as_binary(self):
        return self.ip_to_bin()

    def ip_to_bin(self):
        bin_ip = []
        for octet in self.octets:
            bin_ip.append(bin(int(octet))[2:].zfill(8))
        return ".".join(bin_ip)
    
    def get_octet(self, n):
        if n < 1 or n > 4:
            raise Exception("Invalid octet number")
        else:
            return self.octets[n-1]

    def get_class(self):
        first_octet = int(self.octets[0])
        if first_octet <= 126:
            return "A"
        elif first_octet >= 128 and first_octet <= 191:
            return "B"
        elif first_octet >= 192 and first_octet <= 223:
            return "C"
        elif first_octet >= 224 and first_octet <= 239:
            return "D"
        elif first_octet >= 240 and first_octet <= 255:
            return "E"
        else:
            return "Invalid IP address"

    def is_private(self):
        first_octet = int(self.octets[0])
        second_octet = int(self.octets[1])
        if self.get_class() == "A":
            return first_octet == 10
        elif self.get_class() == "B":
            return first_octet == 172 and 16 <= second_octet <= 31
        elif self.get_class() == "C":
            return first_octet == 192 and second_octet == 168
        else:
            return False

ip_input = input("Enter IP address: ")
ip = NetIPv4(ip_input)
print("IP address:", ip.get_as_string())
print("Valid:", ip.is_valid())
print("Integer:", ip.get_as_int())
print("Binary:", ip.get_as_binary())
print("Octet #2:", ip.get_octet(2))
print("IP Class:", ip.get_class())
print("Private:", ip.is_private())

