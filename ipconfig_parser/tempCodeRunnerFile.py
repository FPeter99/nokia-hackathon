from pathlib import Path
import json

## IPv4 Address. -> ipv4_address
def kulcsFormazas(kulcs) -> str:
    kulcs = kulcs.lower().replace(".", "").strip()
    return kulcs.replace(" ", "_")


## 
def ertekFormazas(v) -> str:
    return v.replace("\ufeff", "").strip().replace("(Preferred)", "").replace("(Deferred)", "").strip()


def fileFormazas(lines):
    adapterek = []
    aktualis = None
    utolsoKulcs = None

    for sor in lines:
        sor = sor.strip()
        if not sor:
            continue

        # objektum kezdete
        if sor.lower().startswith("ethernet adapter") or sor.lower().startswith("wireless lan adapter"):
            if aktualis:
                adapterek.append(aktualis)

            # Extract adapter name from the line (everything after "Adapter ")
            adapter_name = sor.split("adapter ", 1)[1].rstrip(":") if "adapter " in sor.lower() else ""

            ## kezdetben üres
            aktualis = {
                    "adapter_name": adapter_name,
                    "description": "",
                    "physical_address": "",
                    "dhcp_enabled": "",
                    "ipv4_address": "",
                    "subnet_mask": "",
                    "default_gateway": "",
                    "dns_servers": []
                }
            utolsoKulcs = None
            continue

        if aktualis is None:
            continue

        # ha adatsor
        if ":" in sor:
            ## első ":"-nál spliteljük
            k, e = sor.split(":", 1)
            k = kulcsFormazas(k)
            e = ertekFormazas(e)

            utolsoKulcs = k

            if k in ("dns_servers", "default_gateway"):
                aktualis[k] = [e] if e else []
            else:
                aktualis[k] = e

        else:
            # többsoros érték
            if utolsoKulcs in ("dns_servers", "default_gateway"):
                formatted_value = ertekFormazas(sor)
                if formatted_value:
                    aktualis[utolsoKulcs].append(formatted_value)
            elif utolsoKulcs:
                aktualis[utolsoKulcs] = (aktualis[utolsoKulcs] + " " + ertekFormazas(sor)).strip()

    if aktualis:
        adapterek.append(aktualis)

    return adapterek


def egyszerusites(a):
    dg = a.get("default_gateway", [])
    dns = a.get("dns_servers", [])
    return {
        "adapter_name": a.get("adapter_name", ""),
        "description": a.get("description", ""),
        "physical_address": a.get("physical_address", ""),
        "dhcp_enabled": a.get("dhcp_enabled", ""),
        "ipv4_address": a.get("ipv4_address", ""),
        "subnet_mask": a.get("subnet_mask", ""),
        "default_gateway": ", ".join(dg) if dg else "",
        "dns_servers": ", ".join(dns) if dns else ""
    }


def main():
    out = []

    for f in sorted(Path(".").glob("*.txt")):
        sorok = f.read_text(encoding="utf-16", errors="ignore").splitlines()

        adapters = fileFormazas(sorok)

        out.append({
            "file_name": f.name,
            "adapters": [egyszerusites(a) for a in adapters]
        })

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()