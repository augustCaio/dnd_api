from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class Criatura(BaseModel):
    """Modelo para criaturas de D&D 5e."""
    id: str = Field(..., description="Identificador único da criatura (slug)")
    nome: str = Field(..., description="Nome da criatura")
    tipo: str = Field(..., description="Tipo da criatura (ex: besta, elemental, morto-vivo, humanoide, etc.)")
    tamanho: str = Field(..., description="Tamanho da criatura (Miúdo, Pequeno, Médio, Grande, Enorme, Colossal)")
    ca: int = Field(..., description="Classe de Armadura da criatura")
    pv: str = Field(..., description="Pontos de Vida da criatura (ex: '9 (2d8)', '45 (10d8)')")
    deslocamento: str = Field(..., description="Deslocamento da criatura (ex: '9 m', '12 m')")
    atributos: Dict[str, int] = Field(..., description="Atributos da criatura (FOR, DES, CON, INT, SAB, CAR)")
    sentidos: Optional[List[str]] = Field(None, description="Sentidos especiais da criatura")
    idiomas: Optional[str] = Field(None, description="Idiomas que a criatura conhece")
    nivel_desafio: str = Field(..., description="Nível de Desafio da criatura (ex: '1/4', '1', '5')")
    ataques: Optional[List[str]] = Field(None, description="Lista de ataques da criatura")
    notas: Optional[str] = Field(None, description="Notas adicionais sobre a criatura")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "goblin",
                    "nome": "Goblin",
                    "tipo": "Humanoide",
                    "tamanho": "Pequeno",
                    "ca": 15,
                    "pv": "7 (2d6)",
                    "deslocamento": "9 m",
                    "atributos": {
                        "FOR": 8,
                        "DES": 14,
                        "CON": 10,
                        "INT": 10,
                        "SAB": 8,
                        "CAR": 8
                    },
                    "sentidos": [
                        "Visão no escuro 18 m",
                        "Percepção passiva 9"
                    ],
                    "idiomas": "Comum, Goblin",
                    "nivel_desafio": "1/4",
                    "ataques": [
                        "Espada curta. Ataque Corpo a Cor com Arma: +4 para atingir, alcance 1,5 m, um alvo. Acerto: 5 (1d6 + 2) dano de corte."
                    ],
                    "notas": "Goblins são pequenos humanoides que vivem em tribos e são conhecidos por sua astúcia e traição."
                },
                {
                    "id": "dragao-vermelho-adulto",
                    "nome": "Dragão Vermelho Adulto",
                    "tipo": "Dragão",
                    "tamanho": "Enorme",
                    "ca": 19,
                    "pv": "256 (19d12 + 133)",
                    "deslocamento": "12 m, voo 24 m",
                    "atributos": {
                        "FOR": 27,
                        "DES": 14,
                        "CON": 25,
                        "INT": 16,
                        "SAB": 13,
                        "CAR": 21
                    },
                    "sentidos": [
                        "Visão no escuro 18 m",
                        "Percepção passiva 23",
                        "Visão verdadeira 9 m"
                    ],
                    "idiomas": "Comum, Draconiano",
                    "nivel_desafio": "17",
                    "ataques": [
                        "Mordida. Ataque Corpo a Cor com Arma: +14 para atingir, alcance 3 m, um alvo. Acerto: 19 (2d10 + 8) dano de corte mais 7 (2d6) dano de fogo.",
                        "Garra. Ataque Corpo a Cor com Arma: +14 para atingir, alcance 1,5 m, um alvo. Acerto: 15 (2d6 + 8) dano de corte.",
                        "Sopro de Fogo (Recarrega 5-6). O dragão exala fogo em um cone de 18 m. Cada criatura na área deve fazer um teste de resistência de Destreza CD 21. Em caso de falha, sofre 63 (18d6) dano de fogo, ou metade do dano em caso de sucesso."
                    ],
                    "notas": "Dragões vermelhos são os mais temidos e poderosos dos dragões cromáticos. Eles são extremamente gananciosos e territoriais."
                },
                {
                    "id": "esqueleto",
                    "nome": "Esqueleto",
                    "tipo": "Morto-vivo",
                    "tamanho": "Médio",
                    "ca": 13,
                    "pv": "13 (2d8 + 4)",
                    "deslocamento": "9 m",
                    "atributos": {
                        "FOR": 10,
                        "DES": 14,
                        "CON": 15,
                        "INT": 6,
                        "SAB": 8,
                        "CAR": 5
                    },
                    "sentidos": [
                        "Visão no escuro 18 m",
                        "Percepção passiva 9"
                    ],
                    "idiomas": "Entende todos os idiomas que conhecia em vida, mas não pode falar",
                    "nivel_desafio": "1/4",
                    "ataques": [
                        "Espada curta. Ataque Corpo a Cor com Arma: +4 para atingir, alcance 1,5 m, um alvo. Acerto: 5 (1d6 + 2) dano de corte.",
                        "Arco curto. Ataque à Distância com Arma: +4 para atingir, alcance 18/72 m, um alvo. Acerto: 5 (1d6 + 2) dano de perfuração."
                    ],
                    "notas": "Esqueletos são mortos-vivos criados por magia necromântica. Eles são controlados por seus criadores e não sentem dor ou medo."
                }
            ]
        }
    } 