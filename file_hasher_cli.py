import hashlib
import os
import sys

class FileHasherCLI:
    def __init__(self, hashes_file='hashes.txt'):
        self.hashes_file = hashes_file

    def display_menu(self):
        print("\nFile Hasher CLI")
        print("1. Generate and Print Hash")
        print("2. Generate and Save Hash")
        print("3. Compare File Hash")
        print("4. Exit")
        choice = input("Please select an option: ")
        return choice

    def get_file_path(self):
        return input("Path to file: ")

    def get_algorithm(self):
        print("\nAvailable algorithms:")
        for algo in hashlib.algorithms_available:
            print(f" - {algo}")
        algo = input("Enter the algorithm to use (default is sha256): ")
        return algo if algo in hashlib.algorithms_available else 'sha256'

    def generate_hash(self, file_path, algorithm):
        hash_func = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def save_hash(self, file_path, hash_value):
        with open(self.hashes_file, 'a') as f:
            f.write(f"{file_path}: {hash_value}\n")

    def compare_hash(self, file_path, algorithm):
        current_hash = self.generate_hash(file_path, algorithm)
        with open(self.hashes_file, 'r') as f:
            for line in f:
                saved_file_path, saved_hash = line.strip().split(": ")
                if saved_file_path == file_path:
                    return current_hash == saved_hash
        return False

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == '1':
                file_path = self.get_file_path()
                algorithm = self.get_algorithm()
                hash_value = self.generate_hash(file_path, algorithm)
                print(f"\nHash ({algorithm}): {hash_value}")
            elif choice == '2':
                file_path = self.get_file_path()
                algorithm = self.get_algorithm()
                hash_value = self.generate_hash(file_path, algorithm)
                self.save_hash(file_path, hash_value)
                print(f"\nHash saved to {self.hashes_file}")
            elif choice == '3':
                file_path = self.get_file_path()
                algorithm = self.get_algorithm()
                if self.compare_hash(file_path, algorithm):
                    print("\nThe hash values matched.")
                else:
                    print("\nThe hash values did not match.")
            elif choice == '4':
                print("Thank you")
                sys.exit()
            else:
                print("Invalid option.")

if __name__ == "__main__":
    file_hasher_cli = FileHasherCLI()
    file_hasher_cli.run()
