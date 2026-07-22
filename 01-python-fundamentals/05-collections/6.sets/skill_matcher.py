""" Print: Skills common to both candidates.
Skills only Candidate 1 has.
Skills only Candidate 2 has.
All unique skills across both candidates. """

candidate1 = {
    "Python",
    "AWS",
    "Docker",
    "Linux"
}

candidate2 = {
    "Python",
    "Terraform",
    "Linux",
    "Kubernetes"
}

print("skills common to both candidates:", candidate1 & candidate2) # & intersection
print("skills only candidate 1 has:", candidate1 - candidate2) # - difference
print("skills only candidate 2 has:", candidate2 - candidate1)  # - difference
print("all unique skills across both candidates:", candidate1 | candidate2) # | union
