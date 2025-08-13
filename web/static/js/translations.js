// Sistema de Tradução para NeverEndingQuest
// Traduções seguindo os padrões oficiais do D&D em português brasileiro

const translations = {
    // Navegação por abas
    'Character': 'Personagem',
    'Inventory': 'Inventário',
    'Spells & Magic': 'Magias e Magia',
    'NPCs': 'NPCs',
    'Journal': 'Diário',
    'Debug': 'Debug',
    
    // Informações do personagem
    'Level': 'Nível',
    'XP': 'XP',
    'Profession': 'Antecedente',
    'Alignment': 'Tendência',
    'Upload Portrait': 'Enviar Retrato',
    
    // Atributos (seguindo padrão oficial D&D Brasil)
    'STR': 'FOR',
    'DEX': 'DES',
    'CON': 'CON',
    'INT': 'INT',
    'WIS': 'SAB',
    'CHA': 'CAR',
    'Strength': 'Força',
    'Dexterity': 'Destreza',
    'Constitution': 'Constituição',
    'Intelligence': 'Inteligência',
    'Wisdom': 'Sabedoria',
    'Charisma': 'Carisma',
    
    // Estatísticas de combate
    'HP': 'PV',
    'AC': 'CA',
    'INIT': 'INIT',
    'GP': 'PO', // Peças de Ouro
    'SP': 'PP', // Peças de Prata
    'CP': 'PC', // Peças de Cobre
    
    // Seções do personagem
    'Weapons & Attacks': 'Armas e Ataques',
    'Ammunition': 'Munição',
    'Saving Throws': 'Testes de Resistência',
    'Class Features': 'Características de Classe',
    'Features & Traits': 'Características e Traços',
    'CLASS FEATURES': 'CARACTERÍSTICAS DE CLASSE',
    'RACIAL TRAITS': 'TRAÇOS RACIAIS',
    'Racial Traits': 'Traços Raciais',
    'BACKGROUND': 'ANTECEDENTE',
    'Background': 'Antecedente',
    'Active Effects': 'Efeitos Ativos',
    'Feats': 'Talentos',
    'FEATS': 'TALENTOS',
    
    // Features & Traits
    'Ability Score Increase': 'Incremento no Valor de Habilidade',
    'Languages': 'Idiomas',
    'Extra Language': 'Idioma Adicional',
    'SPELLCASTING': 'CONJURAÇÃO',
    
    // Perícias (Skills)
    'Stealth': 'Furtividade',
    'Perception': 'Percepção',
    'Investigation': 'Investigação',
    'Insight': 'Intuição',
    'Persuasion': 'Persuasão',
    'Deception': 'Enganação',
    'Intimidation': 'Intimidação',
    'Performance': 'Atuação',
    'Acrobatics': 'Acrobacia',
    'Sleight of Hand': 'Prestidigitação',
    'Athletics': 'Atletismo',
    'Arcana': 'Arcanismo',
    'History': 'História',
    'Nature': 'Natureza',
    'Religion': 'Religião',
    'Animal Handling': 'Lidar com Animais',
    'Medicine': 'Medicina',
    'Survival': 'Sobrevivência',
    
    // Propriedades de Armas e Equipamentos
    'Finesse': 'Acuidade',
    'Light': 'Leve',
    'Heavy': 'Pesada',
    'Two-handed': 'Duas Mãos',
    'Versatile': 'Versátil',
    'Reach': 'Alcance',
    'Thrown': 'Arremesso',
    'Ammunition': 'Munição',
    'Loading': 'Recarga',
    'Special': 'Especial',
    'Silvered': 'Prateada',
    'Magical': 'Mágica',
    'Adamantine': 'Adamantina',
    'Mithral': 'Mithral',
    
    // Tipos de Dano
    'Slashing': 'Cortante',
    'Piercing': 'Perfurante', 
    'Bludgeoning': 'Contundente',
    'Fire': 'Fogo',
    'Cold': 'Frio',
    'Lightning': 'Relâmpago',
    'Thunder': 'Trovão',
    'Acid': 'Ácido',
    'Poison': 'Veneno',
    'Psychic': 'Psíquico',
    'Necrotic': 'Necrótico',
    'Radiant': 'Radiante',
    'Force': 'Energia',
    
    // Descrições de Características (Tooltips)
    "Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.": "Uma vez por turno, você pode causar 1d6 de dano extra a uma criatura que você atingir com um ataque se você tiver vantagem na jogada de ataque. O ataque deve usar uma arma de acuidade ou à distância. Você não precisa de vantagem na jogada de ataque se outro inimigo do alvo estiver a 1,5 metro dele, esse inimigo não estiver incapacitado e você não tiver desvantagem na jogada de ataque.",
    "You have a military rank from your time as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also gain access to friendly military encampments and fortresses.": "Você tem uma patente militar do seu tempo como soldado. Soldados leais à sua antiga organização militar ainda reconhecem sua autoridade e influência, e eles se submetem a você se forem de uma patente inferior. Você pode invocar sua patente para exercer influência sobre outros soldados e requisitar equipamentos simples ou cavalos para uso temporário. Você também pode ter acesso a acampamentos militares e fortalezas amigáveis.",
    "You can see in dim leve within 60 feet of you as if it were bright leve and in darkness as if it were dim leve": "Você pode ver na penumbra a até 18 metros de você como se fosse luz plena, e na escuridão como se fosse penumbra",
    "You gain proficiency in two skills of your choice. You have chosen Medicine and Survival.": "Você ganha proficiência em duas perícias à sua escolha. Você escolheu Medicina e Sobrevivência.",
    
    // Mensagens de carregamento e status
    'Loading character stats...': 'Carregando estatísticas do personagem...',
    'Loading inventory...': 'Carregando inventário...',
    'Loading spells and magic items...': 'Carregando magias e itens mágicos...',
    'Loading NPC information...': 'Carregando informações de NPCs...',
    'Loading location...': 'Carregando localização...',
    'No character data available': 'Nenhum dado de personagem disponível',
    'No weapons defined.': 'Nenhuma arma definida.',
    'No ammunition.': 'Nenhuma munição.',
    
    // Moedas (seguindo terminologia oficial)
    'Gold': 'Ouro',
    'Silver': 'Prata',
    'Copper': 'Cobre',
    
    // Termos gerais
    'Game Output': 'Saída do Jogo',
    'Connected': 'Conectado',
    'Disconnected': 'Desconectado',
    'Round': 'Rodada',
    'Turn': 'Turno',
    
    // Estatísticas de token (Debug)
    'TPM': 'TPM', // Tokens por minuto
    'RPM': 'RPM', // Requisições por minuto
    'Total': 'Total',
    
    // Tendências (Alinhamentos)
    'Lawful Good': 'Leal e Bom',
    'Neutral Good': 'Neutro e Bom',
    'Chaotic Good': 'Caótico e Bom',
    'Lawful Neutral': 'Leal e Neutro',
    'Neutral': 'Neutro',
    'Chaotic Neutral': 'Caótico e Neutro',
    'Lawful Evil': 'Leal e Mau',
    'Neutral Evil': 'Neutro e Mau',
    'Chaotic Evil': 'Caótico e Mau',
    
    // Classes (algumas principais)
    'Fighter': 'Guerreiro',
    'Wizard': 'Mago',
    'Rogue': 'Ladino',
    'Cleric': 'Clérico',
    'Ranger': 'Patrulheiro',
    'Paladin': 'Paladino',
    'Barbarian': 'Bárbaro',
    'Bard': 'Bardo',
    'Druid': 'Druida',
    'Monk': 'Monge',
    'Sorcerer': 'Feiticeiro',
    'Warlock': 'Bruxo',
    
    // Raças (algumas principais)
    'Human': 'Humano',
    'Elf': 'Elfo',
    'Dwarf': 'Anão',
    'Halfling': 'Halfling',
    'Dragonborn': 'Draconato',
    'Gnome': 'Gnomo',
    'Half-Elf': 'Meio-Elfo',
    'Half-Orc': 'Meio-Orc',
    'Tiefling': 'Tiefling',
    
    // Habilidades e Traços Específicos
    'Expertise': 'Especialização',
    'Sneak Attack': 'Ataque Furtivo',
    'Thieves\' Cant': 'Gíria dos Ladrões',
    'Darkvision': 'Visão no Escuro',
    'Fey Ancestry': 'Ancestralidade Feérica',
    'Skill Versatility': 'Versatilidade em Perícias',
    'Military Rank': 'Patente Militar',
    
    // Armas específicas
    'Shortsword': 'Espada Curta',
    'Dagger': 'Adaga',
    'Shortbow': 'Arco Curto',
    'Arrows': 'Flechas',
    'Longbow': 'Arco Longo',
    'Longsword': 'Espada Longa',
    'Rapier': 'Estoque',
    'Scimitar': 'Cimitarra',
    'Handaxe': 'Machado de Mão',
    'Battleaxe': 'Machado de Batalha',
    'Warhammer': 'Martelo de Guerra',
    'Mace': 'Maça',
    'Club': 'Clava',
    'Quarterstaff': 'Bordão',
    'Spear': 'Lança',
    'Javelin': 'Azagaia',
    'Crossbow': 'Besta',
    'Light Crossbow': 'Besta Leve',
    'Heavy Crossbow': 'Besta Pesada',
    
    // Termos de combate
    'Melee': 'Corpo a Corpo',
    'Ranged': 'À Distância',
    
    // Tipos de equipamentos
    'weapon': 'arma',
    'armor': 'armadura',
    'shield': 'escudo',
    'consumable': 'consumível',
    'misc': 'diversos',
    'magical': 'mágico',
    'tool': 'ferramenta',
    'adventuring gear': 'equipamento de aventura',
    'Equipment': 'Equipamentos',
    'No equipment': 'Nenhum equipamento',
    
    // Armaduras específicas
    'Leather Armor': 'Armadura de Couro',
    'Studded Leather': 'Couro Batido',
    'Chain Mail': 'Cota de Malha',
    'Scale Mail': 'Brunea',
    'Chain Shirt': 'Camisa de Malha',
    'Splint Armor': 'Armadura Segmentada',
    'Plate Armor': 'Armadura de Placas',
    'Shield': 'Escudo',
    
    // Ferramentas e equipamentos
    'Thieves\' Tools': 'Ferramentas de Ladrão',
    'Explorer\'s Pack': 'Pacote do Explorador',
    'Burglar\'s Pack': 'Pacote do Arrombador',
    'Dungeoneer\'s Pack': 'Pacote do Explorador de Masmorras',
    'Entertainer\'s Pack': 'Pacote do Artista',
    'Equipment Pack': 'Pacote de Equipamentos',
    'Backpack': 'Mochila',
    'Bedroll': 'Saco de Dormir',
    'Blanket': 'Cobertor',
    'Tinderbox': 'Caixa de Fogo',
    'Torch': 'Tocha',
    'Rations': 'Rações',
    'Waterskin': 'Cantil',
    'Rope': 'Corda',
    'Grappling Hook': 'Gancho de Escalada',
    'Crowbar': 'Pé de Cabra',
    'Hammer': 'Martelo',
    'Pitons': 'Pitões',
    'Lantern': 'Lanterna',
    'Oil': 'Óleo',
    'Pouch': 'Bolsa',
    'Belt Pouch': 'Bolsa de Cinto',
    'Component Pouch': 'Bolsa de Componentes',
    
    // Itens diversos
    'Common Clothes': 'Roupas Comuns',
    'Fine Clothes': 'Roupas Finas',
    'Traveler\'s Clothes': 'Roupas de Viajante',
    'Gaming Set': 'Conjunto de Jogos',
    'Musical Instrument': 'Instrumento Musical',
    'Artisan\'s Tools': 'Ferramentas de Artesão',
    'Insignia of Rank': 'Insígnia de Patente',
    'Trophy from a fallen enemy': 'Troféu de um Inimigo Caído',
    
    // Elementos do diário/journal
    'Current Objectives': 'Objetivos Atuais',
    'A Chronicle of Deeds': 'Uma Crônica de Feitos',
    'Active Quests': 'Missões Ativas',
    'Completed Quests': 'Missões Concluídas',
    'Journal': 'Diário',
    'Quest Log': 'Registro de Missões'
};

// Padrões de tradução automática para itens não mapeados
const translationPatterns = [
    // Padrões para descrições de armas comuns
    {
        pattern: /^A simple (melee|ranged) weapon(?: with the (.+) propert(?:y|ies))?\.$/i,
        replacement: function(match, weaponType, properties) {
            const typeTranslation = weaponType === 'melee' ? 'corpo a corpo' : 'à distância';
            if (properties) {
                const translatedProps = properties.split(' and ').map(prop => {
                    const cleanProp = prop.replace(/\b(property|properties)\b/g, '').trim();
                    return translations[cleanProp] || cleanProp.toLowerCase();
                }).join(' e ');
                return `Uma arma simples ${typeTranslation} com a propriedade ${translatedProps}.`;
            }
            return `Uma arma simples ${typeTranslation}.`;
        }
    },
    
    // Padrões para descrições gerais de equipamentos
    {
        pattern: /^A (.+) weapon\.$/i,
        replacement: function(match, weaponType) {
            const translatedType = translations[weaponType] || weaponType;
            return `Uma arma ${translatedType}.`;
        }
    },
    
    // Padrões para "You can..." (habilidades)
    {
        pattern: /^You can (.+)\.$/i,
        replacement: function(match, ability) {
            return `Você pode ${ability.toLowerCase()}.`;
        }
    },
    
    // Padrões para "You gain..." (ganhos)
    {
        pattern: /^You gain (.+)\.$/i,
        replacement: function(match, gain) {
            return `Você ganha ${gain.toLowerCase()}.`;
        }
    },
    
    // Padrões para "You have..." (posses)
    {
        pattern: /^You have (.+)\.$/i,
        replacement: function(match, possession) {
            return `Você tem ${possession.toLowerCase()}.`;
        }
    },
    
    // Padrões para "You know..." (conhecimento)
    {
        pattern: /^You know (.+)\.$/i,
        replacement: function(match, knowledge) {
            return `Você conhece ${knowledge.toLowerCase()}.`;
        }
    },
    
    // Padrão específico para Thieves' Cant
    {
        pattern: /^You know thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation\.$/i,
        replacement: "Você conhece a gíria dos ladrões, uma mistura secreta de dialeto, jargão e código que permite esconder mensagens em conversas aparentemente normais."
    },
    
    // Padrões para frases com "that allows you to..."
    {
        pattern: /^(.+) that allows you to (.+)\.$/i,
        replacement: function(match, subject, action) {
            return `${subject.toLowerCase()} que permite ${action.toLowerCase()}.`;
        }
    },
    
    // Padrões para "Once per turn..."
    {
        pattern: /^Once per turn, you (.+)\.$/i,
        replacement: function(match, action) {
            return `Uma vez por turno, você ${action.toLowerCase()}.`;
        }
    },
    
    // Padrões para "At (.+) level..."
    {
        pattern: /^At (\d+)(?:st|nd|rd|th) level, you (.+)\.$/i,
        replacement: function(match, level, action) {
            return `No ${level}º nível, você ${action.toLowerCase()}.`;
        }
    },
    
    // Padrões para "When you (.+), you (.+)"
    {
        pattern: /^When you (.+), you (.+)\.$/i,
        replacement: function(match, condition, result) {
            return `Quando você ${condition.toLowerCase()}, você ${result.toLowerCase()}.`;
        }
    },
    
    // Padrões para propriedades de armas (ex: "Finesse, light.")
    {
        pattern: /^([A-Za-z\s,]+)\.$/, 
        replacement: function(match, properties) {
            return properties.split(', ').map(prop => {
                const trimmed = prop.trim();
                return translations[trimmed] || trimmed;
            }).join(', ') + '.';
        }
    },
    
    // Padrões para descrições de dano (ex: "1d6 slashing damage")
    {
        pattern: /(\d+d\d+)\s+(\w+)\s+damage/gi,
        replacement: '$1 de dano $2'
    },
    
    // Padrões para alcance (ex: "Range 150/600")
    {
        pattern: /Range\s+(\d+)\/(\d+)/gi,
        replacement: 'Alcance $1/$2'
    },
    
    // Padrões para peso (ex: "Weight: 2 lb.")
    {
        pattern: /Weight:\s*(\d+(?:\.\d+)?)\s*lb\./gi,
        replacement: 'Peso: $1 kg'
    },
    // Padrões para armas
    { pattern: /(.+)\s+Sword$/, replacement: 'Espada $1' },
    { pattern: /(.+)\s+Bow$/, replacement: 'Arco $1' },
    { pattern: /(.+)\s+Axe$/, replacement: 'Machado $1' },
    { pattern: /(.+)\s+Hammer$/, replacement: 'Martelo $1' },
    { pattern: /(.+)\s+Crossbow$/, replacement: 'Besta $1' },
    { pattern: /(.+)\s+Dagger$/, replacement: 'Adaga $1' },
    
    // Padrões para armaduras
    { pattern: /(.+)\s+Armor$/, replacement: 'Armadura $1' },
    { pattern: /(.+)\s+Mail$/, replacement: '$1 de Malha' },
    { pattern: /(.+)\s+Leather$/, replacement: 'Couro $1' },
    { pattern: /(.+)\s+Plate$/, replacement: 'Placas $1' },
    
    // Padrões para equipamentos
    { pattern: /(.+)\'s\s+Pack$/, replacement: 'Pacote do $1' },
    { pattern: /(.+)\'s\s+Tools$/, replacement: 'Ferramentas de $1' },
    { pattern: /(.+)\s+Set$/, replacement: 'Conjunto de $1' },
    { pattern: /(.+)\s+Kit$/, replacement: 'Kit de $1' },
    { pattern: /(.+)\s+Pouch$/, replacement: 'Bolsa de $1' },
    
    // Padrões gerais
    { pattern: /^Light\s+(.+)$/, replacement: '$1 Leve' },
    { pattern: /^Heavy\s+(.+)$/, replacement: '$1 Pesada' },
    { pattern: /^Magic\s+(.+)$/, replacement: '$1 Mágica' },
    { pattern: /^Masterwork\s+(.+)$/, replacement: '$1 Obra-Prima' }
];

// Dicionário de traduções de palavras comuns para padrões
const commonWordTranslations = {
    // Propriedades de armas
    'finesse': 'acuidade',
    'light': 'leve', 
    'heavy': 'pesada',
    'versatile': 'versátil',
    'reach': 'alcance',
    'thrown': 'arremesso',
    'ammunition': 'munição',
    'loading': 'recarga',
    'special': 'especial',
    'silvered': 'prateada',
    'magical': 'mágica',
    'simple': 'simples',
    'martial': 'marcial',
    'melee': 'corpo a corpo',
    'ranged': 'à distância',
    'weapon': 'arma',
    'armor': 'armadura',
    'shield': 'escudo',
    
    // Tipos de dano
    'slashing': 'cortante',
    'piercing': 'perfurante',
    'bludgeoning': 'contundente',
    'fire': 'fogo',
    'cold': 'frio',
    'lightning': 'relâmpago',
    'thunder': 'trovão',
    'acid': 'ácido',
    'poison': 'veneno',
    'psychic': 'psíquico',
    'necrotic': 'necrótico',
    'radiant': 'radiante',
    'force': 'energia',
    
    // Palavras gerais
    'Light': 'Leve',
    'Heavy': 'Pesado',
    'Magic': 'Mágico',
    'Masterwork': 'Obra-Prima',
    'Fine': 'Fino',
    'Common': 'Comum',
    'Studded': 'Batido',
    'Chain': 'Malha',
    'Scale': 'Escamas',
    'Splint': 'Segmentado',
    'Plate': 'Placas',
    'Leather': 'Couro',
    'Thieves': 'Ladrão',
    'Explorer': 'Explorador',
    'Burglar': 'Arrombador',
    'Dungeoneer': 'Explorador de Masmorras',
    'Entertainer': 'Artista',
    'Traveler': 'Viajante',
    'Artisan': 'Artesão',
    
    // Palavras de ação e descrição
    'know': 'conhece',
    'allows': 'permite',
    'hide': 'esconder',
    'messages': 'mensagens',
    'conversation': 'conversa',
    'secret': 'secreto',
    'normal': 'normal',
    'seemingly': 'aparentemente',
    'dialect': 'dialeto',
    'jargon': 'jargão',
    'code': 'código',
    'cant': 'gíria',
    'thieves': 'ladrões'
};

// Função para traduzir texto com padrões automáticos
function t(key) {
    if (!key) return key;
    
    // Primeiro, verifica se há tradução direta
    if (translations[key]) {
        return translations[key];
    }
    
    // Tenta aplicar padrões de tradução automática
    for (const pattern of translationPatterns) {
        const match = key.match(pattern.pattern);
        if (match) {
            let result = pattern.replacement;
            
            // Se replacement é função, executa ela
            if (typeof result === 'function') {
                return result(match, ...match.slice(1));
            }
            
            // Se replacement é string, substitui $1, $2, etc.
            if (typeof result === 'string') {
                for (let i = 1; i < match.length; i++) {
                    const translatedGroup = commonWordTranslations[match[i].toLowerCase()] || match[i];
                    result = result.replace(`$${i}`, translatedGroup);
                }
            }
            return result;
        }
    }
    
    // Se não encontrou padrão, tenta traduzir palavras individuais
    const words = key.split(' ');
    if (words.length > 1) {
        const translatedWords = words.map(word => {
            // Remove pontuação para verificar tradução
            const cleanWord = word.replace(/[^\w]/g, '');
            return commonWordTranslations[cleanWord] || word;
        });
        
        // Se alguma palavra foi traduzida, retorna a versão traduzida
        const translatedPhrase = translatedWords.join(' ');
        if (translatedPhrase !== key) {
            return translatedPhrase;
        }
    }
    
    // Se nada funcionou, retorna o original
    return key;
}

// Função para traduzir elementos HTML automaticamente
function translateElement(element) {
    if (element.nodeType === Node.TEXT_NODE) {
        const trimmed = element.textContent.trim();
        if (trimmed && translations[trimmed]) {
            element.textContent = element.textContent.replace(trimmed, translations[trimmed]);
        }
    } else if (element.nodeType === Node.ELEMENT_NODE) {
        // Traduzir atributos específicos se necessário
        if (element.hasAttribute('data-translate')) {
            const key = element.getAttribute('data-translate');
            element.textContent = t(key);
        }
        
        // Processar filhos
        for (let child of element.childNodes) {
            translateElement(child);
        }
    }
}

// Função para traduzir toda a página
function translatePage() {
    translateElement(document.body);
}

// Exportar para uso global
window.t = t;
window.translateElement = translateElement;
window.translatePage = translatePage;
window.translations = translations;
