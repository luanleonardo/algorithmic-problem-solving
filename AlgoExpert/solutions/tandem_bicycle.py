# https://www.algoexpert.io/questions/tandem-bicycle


# O(n log n) time | O(1) space, n = number of riders
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if not fastest:
        return sum(max(s1, s2) for s1, s2 in zip(redShirtSpeeds, blueShirtSpeeds))
    return sum(max(s1, s2) for s1, s2 in zip(redShirtSpeeds, blueShirtSpeeds[::-1]))
