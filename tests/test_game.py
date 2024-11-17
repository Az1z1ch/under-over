import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import GameSession
import filecmp

def run_test_scenario(scenario_file, reference_log_file):
    """
    Запускает тестовый сценарий и сравнивает результаты с эталонным логом
    """
    # Создаем новую игровую сессию
    game = GameSession()
    
    # Читаем и выполняем тестовый сценарий
    with open(scenario_file, 'r') as f:
        test_actions = f.readlines()
    
    # Очищаем текущий лог перед началом теста
    if os.path.exists("logs/game_log.txt"):
        os.remove("logs/game_log.txt")
    
    # Выполняем каждое действие из сценария
    for action in test_actions:
        bet_type, bet_amount = action.strip().split(',')
        game.play(bet_type, int(bet_amount))
    
    # Сравниваем полученный лог с эталонным
    return filecmp.cmp("logs/game_log.txt", reference_log_file)

def main():
    # Путь к тестовым сценариям и эталонным логам
    test_scenarios = [
        ("tests/scenarios/scenario1.txt", "tests/reference_logs/log1.txt"),
        # Добавьте другие сценарии по необходимости
    ]
    
    total_tests = len(test_scenarios)
    passed_tests = 0
    
    for scenario_file, reference_log_file in test_scenarios:
        if run_test_scenario(scenario_file, reference_log_file):
            print(f"Test passed: {scenario_file}")
            passed_tests += 1
        else:
            print(f"Test failed: {scenario_file}")
    
    print(f"\nTotal tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {total_tests - passed_tests}")

if __name__ == "__main__":
    main() 