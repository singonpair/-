import argparse
from typing import Tuple, List

def read_file_contents(file_path: str) -> str:
    """
    Читает содержимое текстового файла.
    
    Args:
        file_path: Путь к файлу.
    
    Returns:
        Содержимое файла в виде строки.
    
    Raises:
        FileNotFoundError: Если файл не найден.
        IOError: При ошибках чтения файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except IOError as e:
        raise IOError(f"Ошибка чтения файла: {e}")

def count_word_occurrences(text: str, word: str) -> Tuple[int, int]:
    """
    Подсчитывает общее количество слов и количество вхождений заданного слова.
    
    Args:
        text: Текст для анализа.
        word: Слово для поиска.
    
    Returns:
        Кортеж (общее количество слов, количество вхождений заданного слова).
    """
    words = text.split()
    total_words = len(words)
    target_word_count = sum(1 for w in words if w.lower() == word.lower())
    return total_words, target_word_count

def main():
    # Настройка парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Поиск слова в текстовом файле.')
    parser.add_argument('file_path', help='Путь к текстовому файлу')
    parser.add_argument('search_word', help='Слово для поиска')
    args = parser.parse_args()
    
    try:
        # Чтение файла
        text = read_file_contents(args.file_path)
        
        # Подсчет слов
        total_words, word_count = count_word_occurrences(text, args.search_word)
        
        # Вывод результатов
        print(f"Общее количество слов в файле: {total_words}")
        print(f"Количество повторений слова '{args.search_word}': {word_count}")
    
    except Exception as e:
        print(f"Ошибка: {e}")

def test_count_word_occurrences():
    """
    Тест для функции count_word_occurrences.
    """
    test_text = "hello world hello Python hello world"
    test_cases = [
        ("hello", 3),
        ("world", 2),
        ("Python", 1),
        ("nonexistent", 0)
    ]
    
    print("\nЗапуск тестов...")
    for word, expected in test_cases:
        _, count = count_word_occurrences(test_text, word)
        assert count == expected, f"Ошибка для слова '{word}': ожидалось {expected}, получено {count}"
        print(f"Тест для '{word}' пройден успешно")
    print("Все тесты пройдены успешно!")

if __name__ == "__main__":
    main()
    # Раскомментируйте следующую строку для запуска тестов
    # test_count_word_occurrences()