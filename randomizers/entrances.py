from dataclasses import dataclass

from wwlib.dzx import DZx, _2DMA, ACTR, PLYR, SCLS
from wwlib.events import EventList

@dataclass(frozen=True)
class ZoneEntrance:
  stage_name: str
  room_num: int
  scls_exit_index: int
  spawn_id: int
  entrance_name: str
  island_name: str = None
  warp_out_stage_name: str = None
  warp_out_room_num: int = None
  warp_out_spawn_id: int = None
  
  @property
  def is_nested(self):
    return self.island_name is None

DUNGEON_ENTRANCES = [
  ZoneEntrance("Adanmae", 0, 2, 2, "Dungeon Entrance on Dragon Roost Island", "Dragon Roost Island", "sea", 13, 211),
  ZoneEntrance("sea", 41, 6, 6, "Dungeon Entrance in Forest Haven Sector", "Forest Haven", "Omori", 0, 215),
  ZoneEntrance("sea", 26, 0, 2, "Dungeon Entrance in Tower of the Gods Sector", "Tower of the Gods", "sea", 26, 1),
  ZoneEntrance("Edaichi", 0, 0, 1, "Dungeon Entrance on Headstone Island", "Headstone Island", "sea", 45, 229),
  ZoneEntrance("Ekaze", 0, 0, 1, "Dungeon Entrance on Gale Isle", "Gale Isle", "sea", 4, 232),
]
BOSS_ENTRANCES = [
  ZoneEntrance("M_NewD2", 10, 1, 27, "Boss Entrance in Dragon Roost Cavern"),
  ZoneEntrance("kindan", 16, 0, 1, "Boss Entrance in Forbidden Woods"),
  ZoneEntrance("Siren", 18, 0, 27, "Boss Entrance in Tower of the Gods"),
  ZoneEntrance("M_Dai", 15, 0, 27, "Boss Entrance in Earth Temple"),
  ZoneEntrance("kaze", 12, 0, 27, "Boss Entrance in Wind Temple"),
]
SECRET_CAVE_ENTRANCES = [
  ZoneEntrance("sea", 44, 8, 10, "Secret Cave Entrance on Outset Island", "Outset Island", "sea", 44, 10),
  ZoneEntrance("sea", 13, 2, 5, "Secret Cave Entrance on Dragon Roost Island", "Dragon Roost Island", "sea", 13, 5),
  # Note: For Fire Mountain and Ice Ring Isle, the spawn ID specified is on the sea with KoRL instead of being at the cave entrance, since the player would get burnt/frozen if they were put at the entrance while the island is still active.
  ZoneEntrance("sea", 20, 0, 0, "Secret Cave Entrance on Fire Mountain", "Fire Mountain", "sea", 20, 0),
  ZoneEntrance("sea", 40, 0, 0, "Secret Cave Entrance on Ice Ring Isle", "Ice Ring Isle", "sea", 40, 0),
  ZoneEntrance("Abesso", 0, 1, 1, "Secret Cave Entrance on Private Oasis", "Private Oasis", "Abesso", 0, 1),
  ZoneEntrance("sea", 29, 0, 5, "Secret Cave Entrance on Needle Rock Isle", "Needle Rock Isle", "sea", 29, 5),
  ZoneEntrance("sea", 47, 1, 5, "Secret Cave Entrance on Angular Isles", "Angular Isles", "sea", 47, 5),
  ZoneEntrance("sea", 48, 0, 5, "Secret Cave Entrance on Boating Course", "Boating Course", "sea", 48, 5),
  ZoneEntrance("sea", 31, 0, 1, "Secret Cave Entrance on Stone Watcher Island", "Stone Watcher Island", "sea", 31, 1),
  ZoneEntrance("sea", 7, 0, 1, "Secret Cave Entrance on Overlook Island", "Overlook Island", "sea", 7, 1),
  ZoneEntrance("sea", 35, 0, 1, "Secret Cave Entrance on Bird's Peak Rock", "Bird's Peak Rock", "sea", 35, 1),
  ZoneEntrance("sea", 12, 0, 1, "Secret Cave Entrance on Pawprint Isle", "Pawprint Isle", "sea", 12, 1),
  ZoneEntrance("sea", 12, 1, 5, "Secret Cave Entrance on Pawprint Isle Side Isle", "Pawprint Isle", "sea", 12, 5),
  ZoneEntrance("sea", 36, 0, 1, "Secret Cave Entrance on Diamond Steppe Island", "Diamond Steppe Island", "sea", 36, 1),
  ZoneEntrance("sea", 34, 0, 1, "Secret Cave Entrance on Bomb Island", "Bomb Island", "sea", 34, 1),
  ZoneEntrance("sea", 16, 0, 1, "Secret Cave Entrance on Rock Spire Isle", "Rock Spire Isle", "sea", 16, 1),
  ZoneEntrance("sea", 38, 0, 5, "Secret Cave Entrance on Shark Island", "Shark Island", "sea", 38, 5),
  ZoneEntrance("sea", 42, 0, 2, "Secret Cave Entrance on Cliff Plateau Isles", "Cliff Plateau Isles", "sea", 42, 2),
  ZoneEntrance("sea", 43, 0, 5, "Secret Cave Entrance on Horseshoe Island", "Horseshoe Island", "sea", 43, 5),
  ZoneEntrance("sea", 2, 0, 1, "Secret Cave Entrance on Star Island", "Star Island", "sea", 2, 1),
]
ALL_ENTRANCES = \
  DUNGEON_ENTRANCES + \
  BOSS_ENTRANCES + \
  SECRET_CAVE_ENTRANCES

@dataclass(frozen=True)
class ZoneExit:
  stage_name: str
  room_num: int
  scls_exit_index: int
  spawn_id: int
  zone_name: str
  unique_name: str
  boss_stage_name: str = None

DUNGEON_EXITS = [
  ZoneExit("M_NewD2", 0, 0, 0, "Dragon Roost Cavern", "Dragon Roost Cavern", "M_DragB"),
  ZoneExit("kindan", 0, 0, 0, "Forbidden Woods", "Forbidden Woods", "kinBOSS"),
  ZoneExit("Siren", 0, 1, 0, "Tower of the Gods", "Tower of the Gods", "SirenB"),
  ZoneExit("M_Dai", 0, 0, 0, "Earth Temple", "Earth Temple", "M_DaiB"),
  ZoneExit("kaze", 15, 0, 15, "Wind Temple", "Wind Temple", "kazeB"),
]
BOSS_EXITS = [
  ZoneExit("M_DragB", 0, 0, 0, "Gohma Boss Arena", "Gohma Boss Arena"),
  ZoneExit("kinBOSS", 0, 0, 0, "Kalle Demos Boss Arena", "Kalle Demos Boss Arena"),
  ZoneExit("SirenB", 0, 0, 0, "Gohdan Boss Arena", "Gohdan Boss Arena"),
  ZoneExit("M_DaiB", 0, 0, 0, "Jalhalla Boss Arena", "Jalhalla Boss Arena"),
  ZoneExit("kazeB", 0, 0, 0, "Molgera Boss Arena", "Molgera Boss Arena"),
]
SECRET_CAVE_EXITS = [
  ZoneExit("Cave09", 0, 1, 0, "Outset Island", "Savage Labyrinth"),
  ZoneExit("TF_06", 0, 0, 0, "Dragon Roost Island", "Dragon Roost Island Secret Cave"),
  ZoneExit("MiniKaz", 0, 0, 0, "Fire Mountain", "Fire Mountain Secret Cave"),
  ZoneExit("MiniHyo", 0, 0, 0, "Ice Ring Isle", "Ice Ring Isle Secret Cave"),
  ZoneExit("TF_04", 0, 0, 0, "Private Oasis", "Cabana Labyrinth"),
  ZoneExit("SubD42", 0, 0, 0, "Needle Rock Isle", "Needle Rock Isle Secret Cave"),
  ZoneExit("SubD43", 0, 0, 0, "Angular Isles", "Angular Isles Secret Cave"),
  ZoneExit("SubD71", 0, 0, 0, "Boating Course", "Boating Course Secret Cave"),
  ZoneExit("TF_01", 0, 0, 0, "Stone Watcher Island", "Stone Watcher Island Secret Cave"),
  ZoneExit("TF_02", 0, 0, 0, "Overlook Island", "Overlook Island Secret Cave"),
  ZoneExit("TF_03", 0, 0, 0, "Bird's Peak Rock", "Bird's Peak Rock Secret Cave"),
  ZoneExit("TyuTyu", 0, 0, 0, "Pawprint Isle", "Pawprint Isle Chuchu Cave"),
  ZoneExit("Cave07", 0, 0, 0, "Pawprint Isle Side Isle", "Pawprint Isle Wizzrobe Cave"),
  ZoneExit("WarpD", 0, 0, 0, "Diamond Steppe Island", "Diamond Steppe Island Warp Maze Cave"),
  ZoneExit("Cave01", 0, 0, 0, "Bomb Island", "Bomb Island Secret Cave"),
  ZoneExit("Cave04", 0, 0, 0, "Rock Spire Isle", "Rock Spire Isle Secret Cave"),
  ZoneExit("ITest63", 0, 0, 0, "Shark Island", "Shark Island Secret Cave"),
  ZoneExit("Cave03", 0, 0, 0, "Cliff Plateau Isles", "Cliff Plateau Isles Secret Cave"),
  ZoneExit("Cave05", 0, 0, 0, "Horseshoe Island", "Horseshoe Island Secret Cave"),
  ZoneExit("Cave02", 0, 0, 0, "Star Island", "Star Island Secret Cave"),
]
ALL_EXITS = \
  DUNGEON_EXITS + \
  BOSS_EXITS + \
  SECRET_CAVE_EXITS

DUNGEON_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS = [
  "Dungeon Entrance on Dragon Roost Island",
]
SECRET_CAVE_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS = [
  "Secret Cave Entrance on Pawprint Isle",
  "Secret Cave Entrance on Cliff Plateau Isles",
]

DUNGEON_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Dragon Roost Cavern",
]
PUZZLE_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Pawprint Isle Chuchu Cave",
  "Ice Ring Isle Secret Cave",
  "Bird's Peak Rock Secret Cave", # Technically this has requirements, but it's just Wind Waker+Wind's Requiem.
  "Diamond Steppe Island Warp Maze Cave",
]
COMBAT_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Rock Spire Isle Secret Cave",
]

ITEM_LOCATION_NAME_TO_EXIT_ZONE_NAME_OVERRIDES = {
  "Pawprint Isle - Wizzrobe Cave": "Pawprint Isle Side Isle",
  "Dragon Roost Cavern - Gohma Heart Container": "Gohma Boss Arena",
  "Forbidden Woods - Kalle Demos Heart Container": "Kalle Demos Boss Arena",
  "Tower of the Gods - Gohdan Heart Container": "Gohdan Boss Arena",
  "Earth Temple - Jalhalla Heart Container": "Jalhalla Boss Arena",
  "Wind Temple - Molgera Heart Container": "Molgera Boss Arena",
}

# TODO: Maybe make a separate list of entrances and exits that have no requirements when you start with a sword. (e.g. Cliff Plateau Isles Secret Cave.) Probably not necessary though.

def randomize_entrances(self):
  if self.options.get("randomize_entrances") == "Dungeons":
    randomize_one_set_of_entrances(self, include_dungeons=True)
  elif self.options.get("randomize_entrances") == "Nested Dungeons":
    randomize_one_set_of_entrances(self, include_dungeons=True, include_bosses=True)
  elif self.options.get("randomize_entrances") == "Secret Caves":
    randomize_one_set_of_entrances(self, include_caves=True)
  elif self.options.get("randomize_entrances") == "Dungeons & Secret Caves (Separately)":
    randomize_one_set_of_entrances(self, include_dungeons=True)
    randomize_one_set_of_entrances(self, include_caves=True)
  elif self.options.get("randomize_entrances") == "Nested Dungeons & Secret Caves (Separately)":
    randomize_one_set_of_entrances(self, include_dungeons=True, include_bosses=True)
    randomize_one_set_of_entrances(self, include_caves=True)
  elif self.options.get("randomize_entrances") == "Dungeons & Secret Caves (Together)":
    randomize_one_set_of_entrances(self, include_dungeons=True, include_caves=True)
  elif self.options.get("randomize_entrances") == "Nested Dungeons & Secret Caves (Together)":
    randomize_one_set_of_entrances(self, include_dungeons=True, include_bosses=True, include_caves=True)
  else:
    raise Exception("Invalid entrance randomizer option: %s" % self.options.get("randomize_entrances"))

def randomize_one_set_of_entrances(self, include_dungeons=False, include_bosses=False, include_caves=False):
  relevant_entrances: list[ZoneEntrance] = []
  relevant_exits: list[ZoneExit] = []
  if include_dungeons:
    relevant_entrances += DUNGEON_ENTRANCES
    relevant_exits += DUNGEON_EXITS
  if include_bosses:
    relevant_entrances += BOSS_ENTRANCES
    relevant_exits += BOSS_EXITS
  if include_caves:
    relevant_entrances += SECRET_CAVE_ENTRANCES
    relevant_exits += SECRET_CAVE_EXITS
  
  remaining_exits = relevant_exits.copy()
  self.rng.shuffle(relevant_entrances)
  
  doing_progress_entrances_for_dungeons_and_caves_only_start = False
  if self.dungeons_and_caves_only_start:
    if include_dungeons and self.options.get("progression_dungeons"):
      doing_progress_entrances_for_dungeons_and_caves_only_start = True
    if include_caves and (self.options.get("progression_puzzle_secret_caves") \
        or self.options.get("progression_combat_secret_caves") \
        or self.options.get("progression_savage_labyrinth")):
      doing_progress_entrances_for_dungeons_and_caves_only_start = True
  
  if self.options.get("race_mode"):
    # Move entrances that are on islands with multiple entrances to the start of the list.
    # This is because we need to prevent these islands from having multiple dungeons on them in Race Mode, and this can fail if they're not at the start of the list because it's possible for the only possibility left to be to put multiple dungeons on one island.
    entrances_not_on_unique_islands = []
    for zone_entrance in relevant_entrances:
      for other_zone_entrance in relevant_entrances:
        if other_zone_entrance.island_name == zone_entrance.island_name and other_zone_entrance != zone_entrance:
          entrances_not_on_unique_islands.append(zone_entrance)
          break
    for zone_entrance in entrances_not_on_unique_islands:
      relevant_entrances.remove(zone_entrance)
    relevant_entrances = entrances_not_on_unique_islands + relevant_entrances
  
  if doing_progress_entrances_for_dungeons_and_caves_only_start:
    # If the player can't access any locations at the start besides dungeon/cave entrances, we choose an entrance with no requirements that will be the first place the player goes.
    # We will make this entrance lead to a dungeon/cave with no requirements so the player can actually get an item at the start.
    
    entrance_names_with_no_requirements = []
    if self.options.get("progression_dungeons"):
      entrance_names_with_no_requirements += DUNGEON_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS
    if self.options.get("progression_puzzle_secret_caves") \
        or self.options.get("progression_combat_secret_caves") \
        or self.options.get("progression_savage_labyrinth"):
      entrance_names_with_no_requirements += SECRET_CAVE_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS
    
    exit_names_with_no_requirements = []
    if self.options.get("progression_dungeons"):
      exit_names_with_no_requirements += DUNGEON_EXIT_NAMES_WITH_NO_REQUIREMENTS
    if self.options.get("progression_puzzle_secret_caves"):
      exit_names_with_no_requirements += PUZZLE_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS
    if self.options.get("progression_combat_secret_caves"):
      exit_names_with_no_requirements += COMBAT_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS
    # No need to check progression_savage_labyrinth, since neither of the items inside Savage have no requirements.
    
    possible_safety_entrances = [
      e for e in relevant_entrances
      if e.entrance_name in entrance_names_with_no_requirements
    ]
    safety_entrance = self.rng.choice(possible_safety_entrances)
    
    # In order to avoid using up all dungeons/caves with no requirements, we have to do this entrance first, so move it to the start of the array.
    relevant_entrances.remove(safety_entrance)
    relevant_entrances.insert(0, safety_entrance)
  
  done_entrances_to_exits: dict[ZoneEntrance, ZoneExit] = {}
  done_exits_to_entrances: dict[ZoneExit, ZoneEntrance] = {}
  while relevant_entrances:
    zone_entrance = relevant_entrances.pop(0)
    outermost_entrance = get_outermost_entrance_for_entrance(zone_entrance, done_exits_to_entrances)
    if outermost_entrance is None:
      # Boss entrance that isn't yet accessible from the sea in any way.
      # We don't want to connect this to anything yet or we risk creating an infinite loop.
      # So postpone it until the end.
      relevant_entrances.append(zone_entrance)
      continue
    
    if doing_progress_entrances_for_dungeons_and_caves_only_start and zone_entrance == safety_entrance:
      possible_remaining_exits = [e for e in remaining_exits if e.unique_name in exit_names_with_no_requirements]
    else:
      possible_remaining_exits = remaining_exits
    
    if any(e for e in possible_remaining_exits if e in DUNGEON_EXITS):
      # Only start placing boss exits after all dungeon exits have been placed.
      possible_remaining_exits = [e for e in remaining_exits if e not in BOSS_EXITS]
    
    # The below is debugging code for testing the caves with timers.
    #if zone_entrance.entrance_name == "Secret Cave Entrance on Fire Mountain":
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name == "Ice Ring Isle Secret Cave"
    #  ]
    #elif zone_entrance.entrance_name == "Secret Cave Entrance on Ice Ring Isle":
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name == "Fire Mountain Secret Cave"
    #  ]
    #else:
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name not in ["Fire Mountain Secret Cave", "Ice Ring Isle Secret Cave"]
    #  ]
    
    if self.options.get("race_mode"):
      # Prevent two entrances on the same island both leading into dungeons (DRC and Pawprint each have two entrances).
      # This is because Race Mode's dungeon markers only tell you what island required dungeons are on, not which of the two entrances it's in. So if a required dungeon and a non-required dungeon were on the same island there would be no way to tell which is required.
      done_entrances_on_same_island_leading_to_a_dungeon = [
        entr for entr in done_entrances_to_exits
        if entr.island_name == zone_entrance.island_name
        and done_entrances_to_exits[entr] in DUNGEON_EXITS
      ]
      if done_entrances_on_same_island_leading_to_a_dungeon:
        possible_remaining_exits = [
          ex for ex in possible_remaining_exits
          if ex not in DUNGEON_EXITS + BOSS_EXITS
        ]
    
    if not possible_remaining_exits:
      raise Exception(f"No valid exits to place for entrance: {zone_entrance.entrance_name}")
    zone_exit = self.rng.choice(possible_remaining_exits)
    remaining_exits.remove(zone_exit)
    
    self.entrance_connections[zone_entrance.entrance_name] = zone_exit.unique_name
    done_entrances_to_exits[zone_entrance] = zone_exit
    done_exits_to_entrances[zone_exit] = zone_entrance
  
  self.logic.update_entrance_connection_macros()
  
  for zone_exit, zone_entrance in done_exits_to_entrances.items():
    outermost_entrance = get_outermost_entrance_for_exit(zone_exit, done_exits_to_entrances)
    
    self.dungeon_and_cave_island_locations[zone_exit.zone_name] = outermost_entrance.island_name
    
    if not self.dry_run:
      update_entrance_to_lead_to_exit(self, zone_entrance, zone_exit, outermost_entrance)
  
  if include_bosses:
    for boss_exit in BOSS_EXITS:
      if not self.dry_run:
        outermost_entrance = get_outermost_entrance_for_exit(boss_exit, done_exits_to_entrances)
        update_boss_warp_out_destination(self, boss_exit.stage_name, outermost_entrance)
  elif include_dungeons:
    for dungeon_exit in DUNGEON_EXITS:
      outermost_entrance = done_exits_to_entrances[dungeon_exit]
      
      if not self.dry_run:
        update_boss_warp_out_destination(self, dungeon_exit.boss_stage_name, outermost_entrance)
      
      # Update the boss exit's island even when nested dungeon randomization is disabled.
      boss_exit = next(
        zone_exit for zone_exit in BOSS_EXITS
        if zone_exit.stage_name == dungeon_exit.boss_stage_name
      )
      self.dungeon_and_cave_island_locations[boss_exit.zone_name] = outermost_entrance.island_name
  
  # Prepare some data so the spoiler log can display the nesting in terms of paths.
  if include_bosses:
    self.nested_entrance_paths = []
    terminal_exits = [ex for ex in relevant_exits if ex not in DUNGEON_EXITS]
    for terminal_exit in terminal_exits:
      zone_entrance = done_exits_to_entrances[terminal_exit]
      seen_entrances = get_all_entrances_on_path_to_entrance(zone_entrance, done_exits_to_entrances)
      path = [terminal_exit.unique_name]
      for entr in seen_entrances:
        path.append(entr.entrance_name)
      path.reverse()
      self.nested_entrance_paths.append(path)

def get_outermost_entrance_for_exit(zone_exit: ZoneExit, done_exits_to_entrances):
  """ Unrecurses nested dungeons to determine what the outermost (island) entrance is for a given exit."""
  zone_entrance = done_exits_to_entrances[zone_exit]
  return get_outermost_entrance_for_entrance(zone_entrance, done_exits_to_entrances)

def get_outermost_entrance_for_entrance(zone_entrance: ZoneEntrance, done_exits_to_entrances):
  """ Unrecurses nested dungeons to determine what the outermost (island) entrance is for a given entrance."""
  seen_entrances = get_all_entrances_on_path_to_entrance(zone_entrance, done_exits_to_entrances)
  if seen_entrances is None:
    return None
  outermost_entrance = seen_entrances[-1]
  return outermost_entrance

def get_all_entrances_on_path_to_entrance(zone_entrance: ZoneEntrance, done_exits_to_entrances):
  """ Unrecurses nested dungeons to build a list of all entrances leading to a given entrance."""
  seen_entrances = []
  while zone_entrance.is_nested:
    if zone_entrance in seen_entrances:
      raise Exception("Entrances are in an infinite loop: %s" % ", ".join([e.entrance_name for e in seen_entrances]))
    seen_entrances.append(zone_entrance)
    dungeon_start_exit = get_dungeon_start_exit_leading_to_nested_entrance(zone_entrance)
    if dungeon_start_exit not in done_exits_to_entrances:
      return None
    zone_entrance = done_exits_to_entrances[dungeon_start_exit]
  seen_entrances.append(zone_entrance)
  return seen_entrances

def get_dungeon_start_exit_leading_to_nested_entrance(zone_entrance: ZoneEntrance):
  assert zone_entrance.entrance_name.startswith("Boss Entrance in ")
  dungeon_name = zone_entrance.entrance_name[len("Boss Entrance in "):]
  dungeon_start_exit = next(ex for ex in DUNGEON_EXITS if ex.unique_name == dungeon_name)
  return dungeon_start_exit

def update_entrance_to_lead_to_exit(self, zone_entrance: ZoneEntrance, zone_exit: ZoneExit, outermost_entrance: ZoneEntrance):
  # Update the stage this entrance takes you into.
  entrance_dzr_path = "files/res/Stage/%s/Room%d.arc" % (zone_entrance.stage_name, zone_entrance.room_num)
  entrance_dzs_path = "files/res/Stage/%s/Stage.arc" % (zone_entrance.stage_name)
  entrance_dzr = self.get_arc(entrance_dzr_path).get_file("room.dzr", DZx)
  entrance_dzs = self.get_arc(entrance_dzs_path).get_file("stage.dzs", DZx)
  entrance_scls = entrance_dzr.entries_by_type(SCLS)[zone_entrance.scls_exit_index]
  entrance_scls.dest_stage_name = zone_exit.stage_name
  entrance_scls.room_index = zone_exit.room_num
  entrance_scls.spawn_id = zone_exit.spawn_id
  entrance_scls.save_changes()
  
  exit_dzr_path = "files/res/Stage/%s/Room%d.arc" % (zone_exit.stage_name, zone_exit.room_num)
  exit_dzs_path = "files/res/Stage/%s/Stage.arc" % zone_exit.stage_name
  
  # Update the DRI spawn to not have spawn type 5.
  # If the DRI entrance was connected to the TotG dungeon, then exiting TotG while riding KoRL would crash the game.
  if len(entrance_dzs.entries_by_type(PLYR)) > 0:
    entrance_spawns = entrance_dzs.entries_by_type(PLYR)
  else:
    entrance_spawns = entrance_dzr.entries_by_type(PLYR)
  entrance_spawn = next(spawn for spawn in entrance_spawns if spawn.spawn_id == zone_entrance.spawn_id)
  if entrance_spawn.spawn_type == 5:
    entrance_spawn.spawn_type = 1
    entrance_spawn.save_changes()
  
  if zone_exit in BOSS_EXITS:
    # Update the spawn you're placed at when saving and reloading inside a boss room.
    exit_dzs = self.get_arc(exit_dzs_path).get_file("stage.dzs", DZx)
    exit_scls = exit_dzs.entries_by_type(SCLS)[zone_exit.scls_exit_index]
    if zone_entrance in BOSS_ENTRANCES:
      # If the end of a dungeon connects to a boss, saving and reloading inside the boss
      # room should put you at the beginning of that dungeon, not the end.
      # But if multiple dungeons are nested we don't take the player all the way back to the
      # beginning of the chain, just to the beginning of the last dungeon.
      dungeon_start_exit = entrance_dzs.entries_by_type(SCLS)[0]
      exit_scls.dest_stage_name = dungeon_start_exit.dest_stage_name
      exit_scls.room_index = dungeon_start_exit.room_index
      exit_scls.spawn_id = dungeon_start_exit.spawn_id
      exit_scls.save_changes()
    else:
      # If a sea entrance connects directly to a boss we put you right outside that entrance.
      exit_scls.dest_stage_name = zone_entrance.stage_name
      exit_scls.room_index = zone_entrance.room_num
      exit_scls.spawn_id = zone_entrance.spawn_id
      exit_scls.save_changes()
  else:
    # Update the entrance you're put at when leaving the dungeon/secret cave.
    exit_dzr = self.get_arc(exit_dzr_path).get_file("room.dzr", DZx)
    exit_scls = exit_dzr.entries_by_type(SCLS)[zone_exit.scls_exit_index]
    exit_scls.dest_stage_name = zone_entrance.stage_name
    exit_scls.room_index = zone_entrance.room_num
    exit_scls.spawn_id = zone_entrance.spawn_id
    exit_scls.save_changes()
  
  # Also update the extra exits when leaving Savage Labyrinth to put you on the correct entrance when leaving.
  if zone_exit.unique_name == "Savage Labyrinth":
    for stage_and_room_name in ["Cave10/Room0", "Cave10/Room20", "Cave11/Room0"]:
      savage_dzr_path = "files/res/Stage/%s.arc" % stage_and_room_name
      savage_dzr = self.get_arc(savage_dzr_path).get_file("room.dzr", DZx)
      exit_sclses = [x for x in savage_dzr.entries_by_type(SCLS) if x.dest_stage_name == "sea"]
      for exit_scls in exit_sclses:
        exit_scls.dest_stage_name = zone_entrance.stage_name
        exit_scls.room_index = zone_entrance.room_num
        exit_scls.spawn_id = zone_entrance.spawn_id
        exit_scls.save_changes()
  
  if zone_exit in SECRET_CAVE_EXITS:
    # Update the sector coordinates in the 2DMA chunk so that save-and-quitting in a secret cave puts you on the correct island.
    exit_dzs = self.get_arc(exit_dzs_path).get_file("stage.dzs", DZx)
    _2dma = exit_dzs.entries_by_type(_2DMA)[0]
    island_number = self.island_name_to_number[outermost_entrance.island_name]
    sector_x = (island_number-1) % 7
    sector_y = (island_number-1) // 7
    _2dma.sector_x = sector_x-3
    _2dma.sector_y = sector_y-3
    _2dma.save_changes()
  
  if zone_exit.unique_name == "Fire Mountain Secret Cave":
    actors = exit_dzr.entries_by_type(ACTR)
    kill_trigger = next(x for x in actors if x.name == "VolTag")
    if zone_entrance.entrance_name == "Secret Cave Entrance on Fire Mountain":
      # Unchanged from vanilla, do nothing.
      pass
    elif zone_entrance.entrance_name == "Secret Cave Entrance on Ice Ring Isle":
      # Ice Ring's entrance leads to Fire Mountain's exit.
      # Change the kill trigger on the inside of Fire Mountain to act like the one inside Ice Ring.
      kill_trigger.type = 2
      kill_trigger.save_changes()
    else:
      # An entrance without a timer leads into this cave.
      # Remove the kill trigger actor on the inside, because otherwise it would throw the player out the instant they enter.
      exit_dzr.remove_entity(kill_trigger, ACTR)
  
  if zone_exit.unique_name == "Ice Ring Isle Secret Cave":
    actors = exit_dzr.entries_by_type(ACTR)
    kill_trigger = next(x for x in actors if x.name == "VolTag")
    if zone_entrance.entrance_name == "Secret Cave Entrance on Ice Ring Isle":
      # Unchanged from vanilla, do nothing.
      pass
    elif zone_entrance.entrance_name == "Secret Cave Entrance on Fire Mountain":
      # Fire Mountain's entrance leads to Ice Ring's exit.
      # Change the kill trigger on the inside of Ice Ring to act like the one inside Fire Mountain.
      kill_trigger.type = 1
      kill_trigger.save_changes()
    else:
      # An entrance without a timer leads into this cave.
      # Remove the kill trigger actor on the inside, because otherwise it would throw the player out the instant they enter.
      exit_dzr.remove_entity(kill_trigger, ACTR)
  
  if zone_exit.unique_name == "Ice Ring Isle Secret Cave":
    # Also update the inner cave of Ice Ring Isle to take you out to the correct entrance as well.
    inner_cave_dzr_path = "files/res/Stage/ITest62/Room0.arc"
    inner_cave_dzr = self.get_arc(inner_cave_dzr_path).get_file("room.dzr", DZx)
    inner_cave_exit_scls = inner_cave_dzr.entries_by_type(SCLS)[0]
    inner_cave_exit_scls.dest_stage_name = zone_entrance.stage_name
    inner_cave_exit_scls.room_index = zone_entrance.room_num
    inner_cave_exit_scls.spawn_id = zone_entrance.spawn_id
    inner_cave_exit_scls.save_changes()
    
    # Also update the sector coordinates in the 2DMA chunk of the inner cave of Ice Ring Isle so save-and-quitting works properly there.
    inner_cave_dzs_path = "files/res/Stage/ITest62/Stage.arc"
    inner_cave_dzs = self.get_arc(inner_cave_dzs_path).get_file("stage.dzs", DZx)
    inner_cave_2dma = inner_cave_dzs.entries_by_type(_2DMA)[0]
    inner_cave_2dma.sector_x = sector_x-3
    inner_cave_2dma.sector_y = sector_y-3
    inner_cave_2dma.save_changes()

def update_boss_warp_out_destination(self, boss_stage_name, outermost_entrance):
  # Update the wind warp out event to take you to the correct island.
  boss_stage_arc_path = "files/res/Stage/%s/Stage.arc" % boss_stage_name
  event_list = self.get_arc(boss_stage_arc_path).get_file("event_list.dat", EventList)
  warp_out_event = event_list.events_by_name["WARP_WIND_AFTER"]
  director = next(actor for actor in warp_out_event.actors if actor.name == "DIRECTOR")
  stage_change_action = next(action for action in director.actions if action.name == "NEXT")
  stage_name_prop = next(prop for prop in stage_change_action.properties if prop.name == "Stage")
  stage_name_prop.value = outermost_entrance.warp_out_stage_name
  room_num_prop = next(prop for prop in stage_change_action.properties if prop.name == "RoomNo")
  room_num_prop.value = outermost_entrance.warp_out_room_num
  spawn_id_prop = next(prop for prop in stage_change_action.properties if prop.name == "StartCode")
  spawn_id_prop.value = outermost_entrance.warp_out_spawn_id

def get_entrance_zone_for_item_location(self, location_name):
  # Helper function to return the entrance zone name for the location.
  #
  # For non-dungeon and non-cave locations, the entrance zone name is simply the zone (island) name. However, when
  # entrances are randomized, the entrance zone name may differ from the zone name for dungeons and caves.
  # As a special case, if the entrance zone is Tower of the Gods or the location name is "Tower of the Gods - Sunken
  # Treasure", the entrance zone name is "Tower of the Gods Sector" to differentiate between the dungeon and the
  # entrance.
  
  zone_name, specific_location_name = self.logic.split_location_name_by_zone(location_name)
  
  if location_name in ITEM_LOCATION_NAME_TO_EXIT_ZONE_NAME_OVERRIDES:
    zone_name = ITEM_LOCATION_NAME_TO_EXIT_ZONE_NAME_OVERRIDES[location_name]
  
  if zone_name in self.dungeon_and_cave_island_locations and self.logic.is_dungeon_or_cave(location_name):
    # If the location is in a dungeon or cave, use the hint for whatever island the dungeon/cave is located on.
    entrance_zone = self.dungeon_and_cave_island_locations[zone_name]
    
    # Special case for Tower of the Gods to use Tower of the Gods Sector when refering to the entrance, not the dungeon
    if entrance_zone == "Tower of the Gods":
      entrance_zone = "Tower of the Gods Sector"
  else:
    # Otherwise, for non-dungeon and non-cave locations, just use the zone name.
    entrance_zone = zone_name
    
    # Special case for Tower of the Gods to use Tower of the Gods Sector when refering to the Sunken Treasure
    if location_name == "Tower of the Gods - Sunken Treasure":
      entrance_zone = "Tower of the Gods Sector"
    # Note that Forsaken Fortress - Sunken Treasure has a similar issue, but there are no randomized entrances on
    # Forsaken Fortress, so we won't make that distinction here.
  
  return entrance_zone
