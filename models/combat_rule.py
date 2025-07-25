class CombatRule:
    def __init__(self, tipo: str, descricao: str):
        self.tipo = tipo
        self.descricao = descricao

class DamageRule(CombatRule):
    def __init__(self, descricao: str):
        super().__init__('dano', descricao)

class AttackRollRule(CombatRule):
    def __init__(self, descricao: str):
        super().__init__('rolagem_ataque', descricao) 