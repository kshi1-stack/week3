#!/usr/bin/env python3
"""
Number Puzzle Solver Game
A logic game that uses arithmetic, comparison, and logical operators
to solve mathematical puzzles and challenges.
"""

import random
import math

class NumberPuzzleGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 10
        
    def display_welcome(self):
        """Display welcome message and game rules"""
        print("=" * 60)
        print("🧮 NUMBER PUZZLE SOLVER GAME 🧮")
        print("=" * 60)
        print("\nWelcome to the Number Puzzle Solver!")
        print("Use arithmetic (+ - * / %), comparison (== != > < >= <=),")
        print("and logical operators (and, or, not) to solve puzzles!")
        print("\nGame Features:")
        print("• Arithmetic puzzles")
        print("• Comparison challenges") 
        print("• Logical reasoning problems")
        print("• Progressive difficulty levels")
        print("\nLet's start! 🎯")
        print("-" * 60)
    
    def arithmetic_puzzle(self):
        """Create arithmetic puzzles using +, -, *, /, % operators"""
        print(f"\n🔢 LEVEL {self.level}: ARITHMETIC PUZZLE")
        print("-" * 40)
        
        # Generate random numbers
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.randint(1, 10)
        
        # Different arithmetic challenges based on level
        if self.level <= 3:
            # Basic operations
            operations = [
                (f"What is {a} + {b}?", a + b),
                (f"What is {a} - {b}?", a - b),
                (f"What is {a} * {c}?", a * c),
                (f"What is {a} / {c}? (integer division)", a // c)
            ]
        elif self.level <= 6:
            # Intermediate with modulo
            operations = [
                (f"What is ({a} + {b}) * {c}?", (a + b) * c),
                (f"What is {a} % {c}?", a % c),
                (f"What is ({a} - {b}) + ({c} * 2)?", (a - b) + (c * 2)),
                (f"What is ({a} * {b}) % {c}?", (a * b) % c)
            ]
        else:
            # Advanced combinations
            operations = [
                (f"What is (({a} + {b}) * {c}) % 10?", ((a + b) * c) % 10),
                (f"What is ({a} ** 2) - ({b} * {c})?", (a ** 2) - (b * c)),
                (f"What is ({a} + {b}) / {c} + ({a} % {c})?", (a + b) // c + (a % c)),
                (f"What is ({a} * {b}) % ({c} + 5)?", (a * b) % (c + 5))
            ]
        
        question, answer = random.choice(operations)
        print(f"Question: {question}")
        
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("✅ Correct! Great job!")
                self.score += 10
                return True
            else:
                print(f"❌ Incorrect. The answer is {answer}")
                return False
        except ValueError:
            print("❌ Please enter a valid number!")
            return False
    
    def comparison_puzzle(self):
        """Create comparison puzzles using ==, !=, >, <, >=, <= operators"""
        print(f"\n⚖️ LEVEL {self.level}: COMPARISON PUZZLE")
        print("-" * 40)
        
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        c = random.randint(1, 20)
        
        # Generate comparison questions
        comparisons = [
            (f"Is {a} == {b}?", a == b),
            (f"Is {a} != {b}?", a != b),
            (f"Is {a} > {b}?", a > b),
            (f"Is {a} < {b}?", a < b),
            (f"Is {a} >= {b}?", a >= b),
            (f"Is {a} <= {b}?", a <= b)
        ]
        
        # Add compound comparisons for higher levels
        if self.level > 3:
            compound_comparisons = [
                (f"Is ({a} + {b}) > ({c} * 3)?", (a + b) > (c * 3)),
                (f"Is ({a} - {b}) <= ({c} + 5)?", (a - b) <= (c + 5)),
                (f"Is ({a} * 2) >= ({b} + {c})?", (a * 2) >= (b + c)),
                (f"Is ({a} % {c}) != ({b} % {c})?", (a % c) != (b % c))
            ]
            comparisons.extend(compound_comparisons)
        
        question, answer = random.choice(comparisons)
        print(f"Question: {question}")
        
        user_input = input("Answer (True/False): ").lower().strip()
        
        if user_input in ['true', 't', 'yes', 'y']:
            user_answer = True
        elif user_input in ['false', 'f', 'no', 'n']:
            user_answer = False
        else:
            print("❌ Please enter True or False!")
            return False
        
        if user_answer == answer:
            print("✅ Correct! Great logical thinking!")
            self.score += 15
            return True
        else:
            print(f"❌ Incorrect. The answer is {answer}")
            return False
    
    def logical_puzzle(self):
        """Create logical puzzles using and, or, not operators"""
        print(f"\n🧠 LEVEL {self.level}: LOGICAL PUZZLE")
        print("-" * 40)
        
        # Generate boolean values
        p = random.choice([True, False])
        q = random.choice([True, False])
        r = random.choice([True, False])
        
        # Different logical challenges
        if self.level <= 3:
            logical_questions = [
                (f"If p = {p} and q = {q}, what is p and q?", p and q),
                (f"If p = {p} and q = {q}, what is p or q?", p or q),
                (f"If p = {p}, what is not p?", not p)
            ]
        elif self.level <= 6:
            logical_questions = [
                (f"If p = {p}, q = {q}, what is (p and q) or (not p)?", (p and q) or (not p)),
                (f"If p = {p}, q = {q}, what is not (p or q)?", not (p or q)),
                (f"If p = {p}, q = {q}, what is (not p) and (not q)?", (not p) and (not q))
            ]
        else:
            logical_questions = [
                (f"If p = {p}, q = {q}, r = {r}, what is (p and q) or (not r)?", (p and q) or (not r)),
                (f"If p = {p}, q = {q}, r = {r}, what is not ((p or q) and r)?", not ((p or q) and r)),
                (f"If p = {p}, q = {q}, r = {r}, what is (p and not q) or (q and r)?", (p and not q) or (q and r))
            ]
        
        question, answer = random.choice(logical_questions)
        print(f"Question: {question}")
        
        user_input = input("Answer (True/False): ").lower().strip()
        
        if user_input in ['true', 't', 'yes', 'y']:
            user_answer = True
        elif user_input in ['false', 'f', 'no', 'n']:
            user_answer = False
        else:
            print("❌ Please enter True or False!")
            return False
        
        if user_answer == answer:
            print("✅ Correct! Excellent logical reasoning!")
            self.score += 20
            return True
        else:
            print(f"❌ Incorrect. The answer is {answer}")
            return False
    
    def conditional_puzzle(self):
        """Create puzzles using if-elif-else conditional logic"""
        print(f"\n🔀 LEVEL {self.level}: CONDITIONAL LOGIC PUZZLE")
        print("-" * 40)
        
        x = random.randint(1, 100)
        
        # Create conditional scenarios
        scenarios = [
            f"Given x = {x}, what will this code output?\n"
            f"if x > 50:\n"
            f"    result = 'high'\n"
            f"elif x > 25:\n"
            f"    result = 'medium'\n"
            f"else:\n"
            f"    result = 'low'",
            
            f"Given x = {x}, what will this code output?\n"
            f"if x % 2 == 0:\n"
            f"    if x > 30:\n"
            f"        result = 'even-big'\n"
            f"    else:\n"
            f"        result = 'even-small'\n"
            f"else:\n"
            f"    result = 'odd'",
            
            f"Given x = {x}, what will this code output?\n"
            f"if x >= 80:\n"
            f"    result = 'A'\n"
            f"elif x >= 60:\n"
            f"    result = 'B'\n"
            f"elif x >= 40:\n"
            f"    result = 'C'\n"
            f"elif x >= 20:\n"
            f"    result = 'D'\n"
            f"else:\n"
            f"    result = 'F'"
        ]
        
        question = random.choice(scenarios)
        print(f"Question: {question}")
        
        # Calculate the correct answer
        if "high" in question:
            if x > 50:
                answer = "high"
            elif x > 25:
                answer = "medium"
            else:
                answer = "low"
        elif "even" in question:
            if x % 2 == 0:
                if x > 30:
                    answer = "even-big"
                else:
                    answer = "even-small"
            else:
                answer = "odd"
        else:  # Grade scenario
            if x >= 80:
                answer = "A"
            elif x >= 60:
                answer = "B"
            elif x >= 40:
                answer = "C"
            elif x >= 20:
                answer = "D"
            else:
                answer = "F"
        
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == answer.lower():
            print("✅ Correct! Great understanding of conditionals!")
            self.score += 25
            return True
        else:
            print(f"❌ Incorrect. The answer is '{answer}'")
            return False
    
    def number_sequence_puzzle(self):
        """Create number sequence puzzles using various operators"""
        print(f"\n🔢 LEVEL {self.level}: NUMBER SEQUENCE PUZZLE")
        print("-" * 40)
        
        # Generate sequences based on level
        if self.level <= 3:
            # Simple arithmetic sequences
            start = random.randint(1, 10)
            sequences = [
                (f"Complete the sequence: {start}, {start+2}, {start+4}, ?", start + 6),
                (f"Complete the sequence: {start}, {start*2}, {start*4}, ?", start * 8),
                (f"Complete the sequence: {start}, {start+5}, {start+10}, ?", start + 15)
            ]
        elif self.level <= 6:
            # Mixed operations
            start = random.randint(1, 20)
            sequences = [
                (f"Complete the sequence: {start}, {start+3}, {start+6}, ?", start + 9),
                (f"Complete the sequence: {start}, {start*2+1}, {start*4+3}, ?", start * 8 + 7),
                (f"Complete the sequence: {start}, {start**2}, {start**3}, ?", start ** 4)
            ]
        else:
            # Complex patterns
            start = random.randint(2, 10)
            sequences = [
                (f"Complete the sequence: {start}, {start*2}, {start*3}, {start*4}, ?", start * 5),
                (f"Complete the sequence: {start}, {start+start}, {start+start*2}, {start+start*3}, ?", start + start * 4),
                (f"Complete the sequence: {start}, {start**2}, {start**3}, ?", start ** 4)
            ]
        
        question, answer = random.choice(sequences)
        print(f"Question: {question}")
        
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("✅ Correct! Great pattern recognition!")
                self.score += 30
                return True
            else:
                print(f"❌ Incorrect. The answer is {answer}")
                return False
        except ValueError:
            print("❌ Please enter a valid number!")
            return False
    
    def play_level(self):
        """Play a complete level with different puzzle types"""
        print(f"\n🎯 STARTING LEVEL {self.level}")
        print("=" * 50)
        
        # Choose puzzle types based on level
        puzzle_types = []
        
        if self.level <= 2:
            puzzle_types = [self.arithmetic_puzzle, self.comparison_puzzle]
        elif self.level <= 4:
            puzzle_types = [self.arithmetic_puzzle, self.comparison_puzzle, self.logical_puzzle]
        elif self.level <= 6:
            puzzle_types = [self.arithmetic_puzzle, self.comparison_puzzle, self.logical_puzzle, self.conditional_puzzle]
        else:
            puzzle_types = [self.arithmetic_puzzle, self.comparison_puzzle, self.logical_puzzle, 
                          self.conditional_puzzle, self.number_sequence_puzzle]
        
        # Play 2-3 puzzles per level
        puzzles_to_solve = min(3, len(puzzle_types))
        puzzles = random.sample(puzzle_types, puzzles_to_solve)
        
        correct_answers = 0
        
        for i, puzzle_func in enumerate(puzzles, 1):
            print(f"\n--- Puzzle {i}/{puzzles_to_solve} ---")
            if puzzle_func():
                correct_answers += 1
        
        # Level completion
        success_rate = correct_answers / puzzles_to_solve
        
        if success_rate >= 0.6:  # 60% success rate to pass
            print(f"\n🎉 LEVEL {self.level} COMPLETED!")
            print(f"Score: {correct_answers}/{puzzles_to_solve} puzzles solved")
            print(f"Total Score: {self.score}")
            return True
        else:
            print(f"\n💪 LEVEL {self.level} FAILED!")
            print(f"Score: {correct_answers}/{puzzles_to_solve} puzzles solved")
            print("Try again to improve your score!")
            return False
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        while self.level <= self.max_level:
            if self.play_level():
                self.level += 1
                if self.level <= self.max_level:
                    print(f"\n🚀 ADVANCING TO LEVEL {self.level}!")
                    input("Press Enter to continue...")
            else:
                retry = input("\nWould you like to retry this level? (y/n): ").lower()
                if retry not in ['y', 'yes']:
                    break
        
        # Game completion
        print("\n" + "=" * 60)
        print("🎊 GAME COMPLETED! 🎊")
        print("=" * 60)
        print(f"Final Score: {self.score}")
        print(f"Levels Completed: {self.level - 1}/{self.max_level}")
        
        if self.level > self.max_level:
            print("🏆 CONGRATULATIONS! You've mastered all levels!")
        else:
            print("💪 Great effort! Try again to complete all levels!")
        
        print("\nThanks for playing Number Puzzle Solver! 🎯")

def main():
    """Main function to start the game"""
    game = NumberPuzzleGame()
    game.play_game()

if __name__ == "__main__":
    main()
