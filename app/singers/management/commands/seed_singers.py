from django.core.management.base import BaseCommand
from singers.models import Singer

SINGERS = [
    "Alok",
    "Bruno Martini",
    "Zeeba",
    "MC Kevinho",
    "Anitta",
    "Pablo Vittar",
    "Matheus e Kauan",
    "Henrique e Juliano",
    "Wesley Safadão",
    "MC Livinho",
    "Jorge e Mateus",
    "Marília Mendonça",
    "Simone e Simaria",
    "Nego do Borel",
    "Henrique e Diego",
    "Maiara e Maraisa",
    "MC G15",
    "MC Fioti",
    "Luan Santana",
    "MC WM",
    "Projota",
    "MC Lan",
    "Léo Santana",
    "Naiara Azevedo",
    "Anavitória",
    "João Neto & Frederico",
    "Lucas Lucco",
    "Dennis DJ",
    "Mc Zaac",
    "Michel Teló",
    "Marcos & Belutti",
    "1Kilo",
    "Bruninho e Davi",
    "Gusttavo Lima",
    "Tribalistas",
    "Mc Don Juan",
    "Knust",
    "Pablo Martins",
    "Ludmilla",
    "Baviera",
    "Os Cretinos",
    "Felipe Araújo",
    "Ivete Sangalo",
    "Bhaskar",
    "Caetano Veloso",
    "Jerry Smith",
    "MC Kekel",
    "Natiruts",
    "Ftampa",
    "Tom Jobim",
    "Fernando & Sorocaba",
    "Tiago Iorc",
    "MC Léléto",
    "Mc Hariel",
    "João Gilberto",
    "Nando Reis",
    "Charlie Brown Jr",
    "Day e Lara",
    "Zé Neto & Cristiano",
    "Bruno & Marrone",
    "Maria Gadú",
    "Turma do Pagode",
    "Cat Dealers",
    "Hungria Hip Hop",
    "Kell Smith",
    "Elis Regina",
    "Marisa Monte",
    "Gilberto Gil",
    "João Bosco & Vinicius",
    "Emicida",
    "Seu Jorge",
    "Djavan",
    "Skank",
    "Roberto Carlos",
    "Cássia Eller",
    "Claudia Leitte",
    "Ana Vilela",
    "Legião Urbana",
    "Bonde R300",
    "Vanessa da Mata",
    "UM44K",
    "Solange Almeida",
    "Jota Quest",
    "O Rappa",
    "Thiaguinho",
    "Jorge Ben Jor",
    "George Henrique & Rodrigo",
    "Lulu Santos",
    "Chico Buarque",
    "Sérgio Mendes",
    "Vintage Culture",
    "Rodrigo Amarante",
    "Sorriso Maroto",
    "Os Paralamas do Sucesso",
    "Capital Inicial",
    "Marcelo D2",
    "Haikaiss",
    "Maneva",
    "Tiê",
    "Oriente",
    "MC Pedrinho",
    "Chitãozinho & Xororó",
    "Delano",
    "Perícles",
    "Kleo Dibah e Rafael",
    "Grupo Revelação",
    "Criolo",
    "Pedro Paulo e Alex",
    "Titãs",
    "Zé Ramalho",
    "DJ Marlboro",
    "Raimundos",
    "Roberta Campos",
    "Maria Rita",
    "Maria Bethânia",
    "Exaltasamba",
    "Cazuza",
    "Preta Gil",
    "Lenine",
    "Ana Carolina",
    "Detonautas Roque Clube",
    "Los Hermanos",
    "Pitty",
    "MC João",
    "Mallu Magalhães",
    "Sandy",
    "Aviões do Forró",
    "Rael",
    "Engenheiros do Hawaii",
    "Dilsinho",
    "Raça Negra",
    "Gal Costa",
    "Armandinho",
    "MC Bin Laden",
    "Zeca Pagodinho",
    "Class A",
    "Evokings",
    "Zezé Di Camargo e Luciano",
    "Martinho da Vila",
    "Zeca Baleiro",
    "Nx Zero",
    "Tropkillaz",
    "Onze:20",
    "TrintaTrinta",
    "Racionais",
    "Thaeme & Thiago",
    "Sepultura",
    "Santti",
    "Guilherme e Santiago",
    "Frejat",
    "Kid Abelha",
    "Alceu Valença",
    "Adriana Calcanhoto",
    "Toquinho",
    "Diogo Nogueira",
    "Elba Ramalho",
    "Jads & Jadson",
    "Mumuzinho",
    "Bruno & Barretto",
    "Cacife Clandestino",
    "Tim Maia",
    "Supercombo",
    "Imaginasamba",
    "Cleber & Cauan",
    "ConeCrewDiretoria",
    "Costa Gold",
    "Thiago Brava",
    "Arlindo Cruz",
    "Scalene",
    "Rita Lee",
    "Karol Conká",
    "Paula Fernandes",
    "Victor e Léo",
    "Belo",
    "Raul Seixas",
    "Beth Carvalho",
    "Loubet",
    "Milton Nascimento",
    "Dani Russo",
    "Eduardo Costa",
    "MC Dede",
    "Lexa",
    "Ana Cañas",
    "Rashid",
    "Gabriel O Pensador",
    "Pixote",
    "Cristiano Araújo",
    "César Menotti e Fabiano",
    "Bom Gosto",
    "Barão Vermelho",
    "Ferrugem",
    "Negra Li",
    "RICCI",
    "Ira",
    "Só Pra Contrariar",
    "MC MM",
    "Roberta Sá",
    "Israel e Rodolffo",
    "Novos Baianos",
    "Edi Rock",
    "Falamansa",
    "Roupa Nova",
    "Paula Mattos",
    "Marcelo Jeneci",
    "Vinicius de Moraes",
    "Aline Barros",
    "Munhoz e Mariano",
    "Grupo Fundo de Quintal",
    "Felipe Ret",
    "Ney Matogrosso",
    "Silva",
    "MC Th",
    "Cidade Negra",
    "MC Guimê",
    "Céu",
    "Jorge Aragão",
    "Clarice Falcão",
    "Chimarruts",
    "A Banda Mais Bonita da Cidade",
    "MC Menor da VG",
    "Fresno",
    "MC Rahell",
    "Humberto & Ronaldo",
    "Márcia Fellipe",
    "Claudinho e Bocheca",
    "Banda do Mar",
    "Fernandinho",
    "MC Kevin",
    "Jorge Vercillo",
    "Mariana Nolasco",
    "Sandy e Junior",
    "Teresa Cristina",
    "CPM.110",
    "Arnaldo Antunes",
    "Nelson Freire",
    "Anderson Freire",
    "Luccas Carlos",
    "Tribo da Periferia",
    "Fagner",
    "Dudu Nobre",
    "Gabriela Rocha",
    "MC Rodolfinho",
    "Zélia Duncan",
    "Pedro e Benicio",
    "Jonas Esticado",
    "OutroEu",
    "Cartola",
    "Andy Bianchini",
    "Conrado & Aleksandro",
    "Valesca Popozuda",
    "Esteban Tavares",
    "Mar Aberto",
    "Preto no Branco",
    "Nossa Toca",
    "Tulipa Ruiz",
    "Os Travessos",
    "MC 2k",
    "Paulo César Baruk",
    "Fred e Gustavo",
    "Felguk",
    "Paulinho da Viola",
    "Perera DJ",
    "Kyber Krystals",
    "Banda Eva",
    "Manu Gavassi",
    "Xamã",
    "Mart’nália",
    "Molejo",
    "Ponto de Equílibrio",
    "Ivan Lins",
    "Maria Cecília e Rodolfo",
    "Planta e Raíz",
    "Leonardo Gonçalves",
    "Marcelo Camelo",
    "Luiz Bonfá",
    "Almir Guineto",
    "Bruna Karla",
    "Tati Zaqui",
    "MC Pikachu",
    "João Brasil",
    "Sabotage",
    "Leandro e Leonardo",
    "Thalles Roberto",
    "Nenhum de Nós",
    "Os Mutantes",
    "Jeito Moleque",
    "Jefferson Moraes",
    "Adoniran Barbosa",
    "Biquini Cavadão",
    "Ministério Zoe",
    "Nara Leão",
    "Davi Sacer",
    "Ego Kill Talent",
    "Mahmundi",
    "MC Brisola",
    "Belchior",
    "Gabriel Camcam",
    "Mamonas Assassinas",
    "Priscilla Alcântara",
    "Ana Gabriela",
    "Gustavo Mioto",
    "Dream Team do Passinho",
    "Secos e Molhados",
    "Fly",
    "Gabriel Diniz",
    "POLLO",
    "Nação Zumbi",
    "Diante do Trono",
    "André Valadão",
    "Eli Soares",
    "Daniela Mercury",
    "Luiz Melodia",
    "Liniker",
    "Daniela Araújo",
    "MC Lustosa",
    "Erasmo Carlos",
    "Pato Fu",
    "Jord",
    "Milionário e José Rico",
    "MV Bill",
    "Fernanda Brum",
    "Rubel",
    "Johnny Hooker",
    "Breno & Caio Cesar",
    "Fábio Jr.",
    "MC Gustta",
    "Inimigos da HP",
    "Rodrigo Marim",
    "João Bosco",
    "Matogrosso e Mathias",
    "Bonde da Stronda",
    "Villa Baggage",
    "Clara Nunes",
    "Gonzaguinha",
    "Biel",
    "Bonde do Tigrão",
    "Art Popular",
    "Rincon Sapiência",
    "DJ Caique",
    "Ultraje a Rigor",
    "Paulinho Moska",
    "Black Alien",
    "Flora Matos",
    "Guilherme Arantes",
    "Os Arrais",
    "Parangolé",
    "Padre Fábio de Melo",
    "MC Hollywood",
    "LIVIT",
    "Júlia & Rafaela",
    "MC Leozinho",
    "Pikeno e Menor",
    "Luan Estilizado",
    "Laura Souguellis",
    "Froid",
    "Daniel",
    "RPM",
    "Eyshila",
    "MC Brinquedo",
    "Bezerra da Silva",
    "Wilson Simonal",
    "Melanina Carioca",
    "Ana Nóbrega",
    "Far From Alaska",
    "Lia Clark",
    "Sofia Oliveira",
    "Wanessa",
    "Bruno Be",
    "Melim",
    "Planet Hemp",
    "Gabriel Guedes de Almeida",
    "Carlinhos Brown",
    "Naldo Benny",
    "Oba Oba Samba House",
    "Forfun",
    "Kelly Key",
    "IZA",
    "Isadora Pompeo",
    "Gabriel Elias",
    "Reinaldo",
    "Renato Russo",
    "Chico César",
    "Nana Caymmi",
    "Jade Baraldo",
    "É o Tchan",
    "Primeiramente",
    "Baco Exu do Blues",
    "Djonga",
    "MC Jhey",
    "MC Marcinho",
    "Vanguart",
    "Rosa de Saron",
    "Psirico",
    "Avine Vinny",
    "Gian e Giovani",
    "Mariana Aydar",
    "Almir Sater",
    "Marcos Valle",
    "Oswaldo Montenegro",
    "Gloria Groove",
    "Chiclete com Banana",
    "João Donato",
    "Elza Soares",
    "Dona Ivone Lara",
    "MC CL",
    "A Banca.414",
    "Luiza Possi",
    "Luisa Sonza",
    "Chico Science",
    "Harmonia do Samba",
    "Koringa",
    "Jão",
    "Aline Calixto",
    "MC Pocahontas",
    "Tom Zé",
    "O Teatro Mágico",
    "Dadá Boladão",
    "Luiz Lins",
    "Marcos & Fernando",
    "Ravena",
    "Angra",
    "Vitor Kley",
    "Toque no Altar",
    "MC Dudu",
    "Jammil",
    "Edu Chociay",
    "Xande de Pilares",
    "Zimbra",
    "Marcello Gugu",
    "Dorgival Dantas",
    "RZO",
    "Luma Elpidio",
    "Maglore",
    "Heloisa Rosa",
    "Padre Marcelo Rossi",
    "Menor",
    "Bokaloka",
    "Guilherme de Sá",
    "Tihuana",
    "Rick e Renner",
    "Chico Rey e Paraná",
    "Edson e Hudson",
    "Daya Luz",
    "Little Joy",
    "Mariana Fagundes",
    "Xuxa",
    "Maysa",
    "MC Phe Cachorrera",
    "Banda Uó",
    "Maykow e Bruno",
    "As Bahias e a Cozinha Mineira",
    "Kleber Lucas",
    "Reginaldo Rossi",
    "Filipe Labre",
    "Marcelo CIC",
    "Oficina G3",
    "Mc Gui",
    "BRAZA",
    "Matanza",
    "Rodolfo Abrantes",
    "Elekfantz",
    "Fernanda Takai",
    "Dalsin",
    "DJ PV",
    "Marina Lima",
    "Pentagono",
    "Paulo Ricardo",
    "Joyce",
    "Ana Muller",
    "Blitz",
    "Banda Calypso",
    "MC Mirella",
    "MOB79",
    "Geo",
    "Calcinha Preta",
    "João Paulo e Daniel",
    "Strike",
    "Vingadora",
    "BK",
    "Phill Veras",
    "Katinguelê",
    "Dj Batata",
    "Apanhador Só",
    "Sinara",
    "Tribo de Jah",
    "Beto Guedes",
    "Ara Ketu",
    "Otto",
    "Don L",
    "Alice Caymmi",
    "Dorival Caymmi",
    "Gabily",
    "Mano Brown",
    "Soweto",
    "Tchakabum",
    "Gabriel Gava",
    "Rodriguinho",
    "O Terno",
    "Cristina Mel",
    "Babado Novo",
]

class Command(BaseCommand):
    help = "Seed Singers on Database"

    def handle(self, *args, **options):
        for singer in SINGERS:
            Singer.objects.get_or_create(name=singer)
