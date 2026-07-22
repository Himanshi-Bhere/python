""" Tasks: Convert the list into a set.
Print all unique visitors.
Print the total number of unique visitors.
Check whether "Sara" visited.
Add "Alex".
Remove "Rahul" using discard()."""

visitors = [
    "Himanshi",
    "Rahul",
    "Sara",
    "Rahul",
    "Amit",
    "Sara",
    "Himanshi"
]

unique_visitors = set(visitors)
print("Unique visitors:", unique_visitors)
print("Total number of unique visitors:", len(unique_visitors))
print("Did Sara visit?", "Sara" in unique_visitors)
unique_visitors.add("Alex")
print("After adding Alex:", unique_visitors)
unique_visitors.discard("Rahul")
print("After removing Rahul:", unique_visitors)