import streamlit as st
import json
from PIL import Image

# ========== Initialize App ==========
st.title("⚔️ Stelo Vienas Armor Customizer ⚔️")
st.sidebar.header("Customize Your Armor")

# ========== Display Armor Diagram ==========
st.sidebar.subheader("Armor Layers Reference")
try:
    image = Image.open("static_armor_diagram.png")
    st.sidebar.image(image, caption="Armor Layers Reference", use_column_width=True)
except FileNotFoundError:
    st.sidebar.error("Armor diagram image not found. Please ensure 'static_armor_diagram.png' is in the application directory.")

# ========== Gender Selection ==========
st.sidebar.subheader("🛡️ Select Gender")
gender = st.sidebar.radio("Character Gender", ["Male", "Female"], key="gender_selection")

# ========== Faction-Based Presets ==========
st.sidebar.subheader("🏰 Select Faction Preset")
factions = {
    "None": {},
    "Arkellion": {"Helmet": "Great Helm", "Chestplate": "Plate Armor", "Cape": "Royal Cloak", "Weapon": "Longsword"},
    "Etheresian": {"Helmet": "Sallet", "Chestplate": "Brigandine", "Cape": "Fur Mantle", "Weapon": "Rapier"},
    "Caracian": {"Helmet": "Morion", "Chestplate": "Scale Armor", "Cape": "Tattered Cloak", "Weapon": "Warhammer"},
    "Vontharian": {"Helmet": "Bascinet", "Chestplate": "Lamellar Armor", "Cape": "Battle Cape", "Weapon": "Battle Axe"},
    "Sukhalan": {"Helmet": "Kettle Helm", "Chestplate": "Kavacha (South Indian)", "Cape": "None", "Weapon": "Scimitar"}
}
selected_faction = st.sidebar.selectbox("Faction Preset", list(factions.keys()), key="faction_preset")

# ========== Armor Options ==========
armor_options = {
    "Helmet": ["None", "Barbute", "Armet", "Spangenhelm", "Kula (South Indian)", "Nasal Helm", "Great Helm", "Close Helm", "Sallet", "Bascinet", "Morion", "Kettle Helm", "Horned Helm", "Winged Helm"],
    "Base Layer": ["None", "Gambeson", "Padded Gambeson", "Chainmail", "Leather Jerkin"],
    "Over Layer": ["None", "Surcoat", "Tabard", "Hooded Cloak"],
    "Chestplate": ["None", "Lorica Segmentata", "Scale Armor", "Kavacha (South Indian)", "Plate Armor", "Brigandine", "Lamellar Armor"],
    "Pauldrons": ["None", "Pteruges (Roman)", "Winged Pauldrons", "Spiked Pauldrons", "Fluted Pauldrons", "Dragon-scale Pauldrons"],
    "Metal Gauntlets": ["None", "Steel Claws", "Plate Gauntlets", "Splinted Gauntlets"],
    "Leather/Cloth Gauntlets": ["None", "Finger Gauntlets", "Chainmail Mittens", "Demon Claws"],
    "Greaves": ["None", "Leather Greaves", "Steel Greaves", "Bronze Shin Guards", "Plated Tassets", "Dragonbone Greaves"],
    "Cape": ["None", "Tattered Cloak", "Fur Mantle", "Battle Cape", "Royal Cloak"],
    "Weapon": ["None", "Longsword", "Rapier", "Warhammer", "Battle Axe", "Scimitar", "Spear", "Greatsword", "Mace", "Dagger", "Crossbow"],
    "Engraving": ["None", "Runes", "Heraldic Crest", "Floral Motif", "Battle Scars"],
    "Armor Condition": ["Pristine", "Battle-Worn", "Damaged"]
}

# ========== Material Options ==========
material_options = {
    "Metals": ["Steel", "Iron", "Bronze", "Copper", "Brass", "Aluminum", "Titanium", "Nickel", "Silver", "Gold", "Mithril", "Orichalcum", "Adamantium"],
    "Cloth/Leather": ["Cotton", "Linen", "Wool", "Silk", "Canvas", "Velvet", "Burlap", "Denim", "Twill", "Damask", "Leather", "Suede", "Fur"]
}

# ========== Initialize user_armor Dictionary ==========
if 'user_armor' not in st.session_state:
    st.session_state.user_armor = {category: {"Type": "None", "Material": "None", "Color": "#808080", "Layer": "Over"} for category in armor_options}

# ========== Apply Faction Preset if Selected ==========
if selected_faction != "None":
    preset = factions[selected_faction]
    for key, value in preset.items():
        st.session_state.user_armor[key]["Type"] = value

# ========== Armor Customization ==========
st.sidebar.subheader("🛠️ Customize Each Armor Piece")
for category, choices in armor_options.items():
    st.session_state.user_armor[category]["Type"] = st.sidebar.selectbox(f"{category} Type", choices, key=f"{category}_type")
    if category in ["Helmet", "Chestplate", "Pauldrons", "Metal Gauntlets", "Greaves", "Weapon"]:
        material_category = "Metals"
    else:
        material_category = "Cloth/Leather"
    st.session_state.user_armor[category]["Material"] = st.sidebar.selectbox(f"{category} Material", material_options[material_category], key=f"{category}_material")
    st.session_state.user_armor[category]["Color"] = st.sidebar.color_picker(f"{category} Color", "#808080", key=f"{category}_color")
    st.session_state.user_armor[category]["Layer"] = st.sidebar.radio(f"{category} Layer Position", ["Over", "Under"], key=f"{category}_layer")

# ========== Pre-Generated Random Presets ==========
st.sidebar.subheader("🎲 Random Pre-Generated Armor Sets")
random_presets = [
    {"Helmet": "Great Helm", "Chestplate": "Plate Armor", "Cape": "Royal Cloak", "Weapon": "Longsword"},
    {"Helmet": "Sallet", "Chestplate": "Brigandine", "Cape": "Fur Mantle", "Weapon": "Rapier"},
    {"Helmet": "Morion", "Chestplate": "Scale Armor", "Cape": "Tattered Cloak", "Weapon": "Warhammer"},
    {"Helmet": "Bascinet", "Chestplate": "Lamellar Armor", "Cape": "Battle Cape", "Weapon": "Battle Axe
::contentReference[oaicite:0]{index=0}
 

 
