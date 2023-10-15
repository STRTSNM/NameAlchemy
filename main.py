import random

def load_names_from_file(filename):
    try:
        with open(filename) as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def generate_combined_names(name_list, n):
    combined_names = []
    for _ in range(n):
        name1, name2 = random.sample(name_list, 2)
        combined_name = name1 + name2
        combined_names.append(combined_name)
        print(f'   ---> {combined_name}')
    return combined_names

def save_to_file(filename, generated_names):
    try:
        with open(filename, 'w') as f:
            for name in generated_names:
                f.write(name + '\n')
        print(f"Generated names saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def main(n):
    name_list = load_names_from_file('list.txt')
    if not name_list:
        return
    print("Names:")
    combined_names = generate_combined_names(name_list, n)

    save_option = input("Do you want to save the generated names to a file? (yes/no): ")
    if save_option.lower() == "yes":
        save_filename = input("Enter a filename to save the generated names: ")
        save_to_file(save_filename, combined_names)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Number of names: "))
            main(n)
        except KeyboardInterrupt:
            print("\nBye!\n")
            exit()
        except ValueError:
            print("Please enter a valid number.")

