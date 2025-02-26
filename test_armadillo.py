import unittest
from sapai import *

class TestArmadillo(unittest.TestCase):
    def test_armadillo_start_of_battle(self):
        # Create two teams with multiple pets
        team1 = Team(["fish", "beaver", "armadillo"])
        team2 = Team(["cricket", "horse"])# Opposing team
        
        # Store initial health of all pets
        team1_initial_health = [pet.pet.health for pet in team1 if not pet.empty]
        team2_initial_health = [pet.pet.health for pet in team2 if not pet.empty]
        
        # Start battle
        battle = Battle(team1, team2)
        battle.start()
        
        # After battle starts, check health of all pets
        # Each pet should have +8 health from level 1 armadillo
        for idx, slot in enumerate(battle.t0):
            if not slot.empty:
                expected_health = team1_initial_health[idx] + 8
                self.assertEqual(
                    slot.pet.health,
                    expected_health,
                    f"Team 1 {slot.pet.name} should have {expected_health} health (initial + 8)"
                )
                
        for idx, slot in enumerate(battle.t1):
            if not slot.empty:
                expected_health = team2_initial_health[idx] + 8
                self.assertEqual(
                    slot.pet.health,
                    expected_health,
                    f"Team 2 {slot.pet.name} should have {expected_health} health (initial + 8)"
                )

    def test_multiple_armadillos(self):
        # Test that multiple armadillos stack their effects
        team1 = Team(["armadillo", "armadillo", "fish"])  # Team with 2 armadillos
        team2 = Team(["cricket", "horse"])  # Opposing team
        
        # Store initial health
        team1_initial_health = [pet.pet.health for pet in team1 if not pet.empty]
        team2_initial_health = [pet.pet.health for pet in team2 if not pet.empty]
        
        # Start battle
        battle = Battle(team1, team2)
        battle.start()
        # Each pet should have +16 health (8 from each armadillo)
        for idx, slot in enumerate(battle.t0):
            if not slot.empty:
                expected_health = team1_initial_health[idx] + 16
                self.assertEqual(
                    slot.pet.health,
                    expected_health,
                    f"Team 1 {slot.pet.name} should have {expected_health} health (initial + 16)"
                )
                
        for idx, slot in enumerate(battle.t1):
            if not slot.empty:
                expected_health = team2_initial_health[idx] + 16
                self.assertEqual(
                    slot.pet.health,
                    expected_health,
                    f"Team 2 {slot.pet.name} should have {expected_health} health (initial + 16)"
                )

    def test_leveled_armadillo(self):
        # Test that a level 2 armadillo gives +16 health to all pets
        team1 = Team(["fish", "beaver"])
        team2 = Team(["cricket", "horse"])
        
        # Add a level 2 armadillo to team1
        armadillo = Pet("armadillo")
        armadillo.level = 2
        team1.append(armadillo)
        
        # Store initial health
        team1_initial_health = [pet.pet.health for pet in team1 if not pet.empty]
        team2_initial_health = [pet.pet.health for pet in team2 if not pet.empty]
        
        # Start battle
        battle = Battle(team1, team2)
        battle.start()
        # Each pet should have +16 health from level 2 armadillo
        for idx, slot in enumerate(battle.t0):
            if not slot.empty:
                expected_health = team1_initial_health[idx] + 16
                self.assertEqual(
                    slot.pet.health,
                    expected_health,
                    f"Team 1 {slot.pet.name} should have {expected_health} health (initial + 16)"
                )
                
        for idx, slot in enumerate(battle.t1):
            if not slot.empty:
                expected_health = team2_initial_health[idx] + 16
                self.assertEqual(
                    slot.pet.health,
                    expected_health,
                    f"Team 2 {slot.pet.name} should have {expected_health} health (initial + 16)"
                )

if __name__ == '__main__':
    unittest.main()

