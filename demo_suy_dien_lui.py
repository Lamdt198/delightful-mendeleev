# -*- coding: utf-8 -*-
"""
DEMO 1: THUAT TOAN SUY DIEN LUI (BACKWARD CHAINING)
Dua theo quy trinh 4 buoc trong slide:
  B1: Lay cac thong tin ve bai toan va dat vao bo nho lam viec (WM).
  B2: Kiem tra trong bo nho lam viec xem dich da duoc bo sung truoc do chua.
  B3: Neu co trong bo nho thi dung lai. Nguoc lai tim cac luat co ket luan chua dich.
  B4: Kiem tra phan gia thiet cua luat; neu chua co thi goi la dich moi (dich con)
      va lap lai qua trinh.
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class Rule:
    def __init__(self, name, premises, conclusion, description=""):
        self.name = name                      # Ten luat (vi du: R1, R2)
        self.premises = list(premises)        # Cac gia thiet (ve trai IF)
        self.conclusion = conclusion          # Ket luan (ve phai THEN)
        self.description = description        # Mo ta y nghia

    def __repr__(self):
        return f"[{self.name}] IF {' AND '.join(self.premises)} THEN {self.conclusion}"


class BackwardChainingEngine:
    def __init__(self, rules, initial_facts):
        self.rules = rules
        self.working_memory = set(initial_facts)  # Bo nho lam viec (Facts da biet)
        self.step_counter = 1
        self.proof_tree = []                      # Luu vet cac buoc chung minh

    def log_step(self, message, indent=0):
        prefix = "   " * indent
        print(f"[Bước {self.step_counter:02d}] {prefix}{message}")
        self.step_counter += 1

    def solve(self, goal, depth=0):
        """
        Thuc thi suy dien lui de chung minh muc tieu (goal).
        Tra ve True neu chung minh duoc, False neu khong the.
        """
        self.log_step(f"--> Kiem tra muc tieu can chung minh: '{goal}'", depth)

        # B2 & B3: Kiem tra trong bo nho lam viec (Working Memory)
        if goal in self.working_memory:
            self.log_step(f"[THANH CONG] '{goal}' DA CO SAN trong Bo nho lam viec!", depth)
            self.proof_tree.append((depth, f"'{goal}' co san trong tap gia thiet ban dau"))
            return True

        # B3 (nguoc lai): Tim cac luat co phan ket luan chua dich
        candidate_rules = [r for r in self.rules if r.conclusion == goal]

        if not candidate_rules:
            self.log_step(f"[THAT BAI] Khong co luat nao co ket luan la '{goal}'!", depth)
            return False

        self.log_step(
            f"Tim thay {len(candidate_rules)} luat cho ra '{goal}': {[r.name for r in candidate_rules]}", 
            depth
        )

        # B4: Kiem tra phan gia thiet cua cac luat nay
        for rule in candidate_rules:
            self.log_step(f"Thu ap dung luat {rule}:", depth)
            all_premises_proven = True

            for premise in rule.premises:
                self.log_step(f"Tao dich con moi: can chung minh '{premise}' cho luat {rule.name}", depth + 1)
                
                # De quy chung minh dich con
                proven = self.solve(premise, depth + 1)
                if not proven:
                    self.log_step(f"Khong the chung minh gia thiet '{premise}' cho luat {rule.name}", depth + 1)
                    all_premises_proven = False
                    break

            if all_premises_proven:
                # Tat ca gia thiet cua luat da duoc chung minh
                self.working_memory.add(goal)
                self.log_step(f"[KET LUAN] Luat {rule.name} thoa man! Bo sung '{goal}' vao Bo nho lam viec.", depth)
                self.proof_tree.append((depth, f"Ap dung {rule} ==> Rut ra '{goal}'"))
                return True

        return False


def run_demo():
    print("=" * 65)
    print("DEMO SUY DIEN LUI (BACKWARD CHAINING) - HE CHUYEN GIA")
    print("=" * 65)

    # 1. Dinh nghia tap luat cua he thong
    rules = [
        Rule("R1", ["Sốt", "Đau_họng"], "Viêm_họng", "Nếu sốt và đau họng thì bị viêm họng"),
        Rule("R2", ["Viêm_họng", "Khó_thở"], "Nhiễm_trùng_hô_hấp", "Nếu viêm họng và khó thở thì nhiễm trùng"),
        Rule("R3", ["Nhiệt_độ_cao"], "Sốt", "Nếu nhiệt độ cao thì là bị sốt"),
        Rule("R4", ["Ho_khan", "Mệt_mỏi"], "Cảm_cúm", "Nếu ho khan và mệt mỏi thì cảm cúm"),
        Rule("R5", ["Nhiễm_trùng_hô_hấp"], "Cần_nhập_viện", "Nếu nhiễm trùng hô hấp thì cần nhập viện")
    ]

    # 2. Tap su kien ban dau (B1: Bo nho lam viec - Working Memory)
    initial_facts = ["Nhiệt_độ_cao", "Đau_họng", "Khó_thở"]
    goal = "Cần_nhập_viện"

    print("\n--- 1. CAU HINH BAI TOAN ---")
    print("DANH SACH CAC LUAT (KNOWLEDGE BASE):")
    for r in rules:
        print(f"  {r}  ({r.description})")

    print(f"\nBO NHO LAM VIEC BAN DAU (WORKING MEMORY): {initial_facts}")
    print(f"MUC TIEU CAN CHUNG MINH (GOAL): '{goal}'")
    print("\n--- 2. QUA TRINH SUY DIEN LUI (THEO 4 BUOC TRONG SLIDE) ---")

    engine = BackwardChainingEngine(rules, initial_facts)
    success = engine.solve(goal)

    print("\n--- 3. KET QUA SUY DIEN ---")
    if success:
        print(f"==> KET QUA: CHUNG MINH THANH CONG!")
        print(f"Muc tieu '{goal}' la DUNG.")
        print("\nCAY TRUY VET SUY DIEN (PROOF TRACE):")
        for depth, log in engine.proof_tree:
            indent = "  " * depth
            print(f"  {indent}* {log}")
    else:
        print(f"==> KET QUA: THAT BAI! Khong the chung minh '{goal}' tu tap gia thiet da cho.")

    print(f"\nBO NHO LAM VIEC SAU KHI SUY DIEN: {sorted(list(engine.working_memory))}")
    print("=" * 65)

if __name__ == "__main__":
    run_demo()
