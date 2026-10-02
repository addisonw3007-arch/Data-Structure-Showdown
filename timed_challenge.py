# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# Problem 3: Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

def remove_duplicates(values):
        seen = set()
        result = []

        for value in values:
            if value not in seen:
                seen.add(value)
                result.append(value)
        
        return result

print(remove_duplicates(["apple", "banana", "apple", "kiwi", "banana"]))
print(remove_duplicates([]))
print(remove_duplicates(["apple", "apple", "apple"]))

