# Java Collections Framework - Study Guide

## Introduction to Collections

The **Java Collections Framework** is a unified architecture for representing and manipulating groups of objects. Instead of using basic arrays, collections provide flexible and efficient data structures like Lists, Sets, Queues, and Maps.

### Key Benefits:
- **Reusability**: Pre-built, tested implementations
- **Flexibility**: Multiple data structures for different use cases
- **Performance**: Optimized for different operations
- **Consistency**: Common interface across different collection types

### Common Collection Types:
- **List**: Ordered collection (LinkedList, ArrayList)
- **Set**: Unique elements (HashSet, TreeSet)
- **Queue**: FIFO operations (PriorityQueue, Deque)
- **Map**: Key-value pairs (HashMap, TreeMap)

---

## List Interface (Common Methods)

| Command | Description | Example | Return Type |
|---------|-------------|---------|-------------|
| `.add(element)` | Adds element to the end | `list.add("item")` | boolean |
| `.add(index, element)` | Inserts at specific index | `list.add(0, "item")` | void |
| `.set(index, element)` | Replaces element at index | `list.set(0, "new")` | Object |
| `.get(index)` | Gets element at index | `list.get(0)` | Object |
| `.remove(index)` | Removes element at index | `list.remove(0)` | Object |
| `.remove(element)` | Removes first occurrence | `list.remove("item")` | boolean |
| `.clear()` | Removes all elements | `list.clear()` | void |
| `.size()` | Returns number of elements | `list.size()` | int |
| `.isEmpty()` | Checks if empty | `list.isEmpty()` | boolean |
| `.contains(element)` | Checks if element exists | `list.contains("item")` | boolean |
| `.indexOf(element)` | Gets index of first occurrence | `list.indexOf("item")` | int |
| `.lastIndexOf(element)` | Gets index of last occurrence | `list.lastIndexOf("item")` | int |
| `.subList(fromIndex, toIndex)` | Gets subset of list | `list.subList(0, 2)` | List |
| `.sort(comparator)` | Sorts the list | `list.sort(null)` | void |

**Note**: `List` is an interface implemented by `ArrayList`, `LinkedList`, `Vector`, etc.

---

## LinkedList Commands Reference

| Command | Description | Example | Return Type |
|---------|-------------|---------|-------------|
| `.add(element)` | Adds element to the end | `playlist.add("Song1")` | boolean |
| `.addFirst(element)` | Adds element at the beginning | `playlist.addFirst("Song1")` | void |
| `.addLast(element)` | Adds element at the end | `playlist.addLast("Song1")` | void |
| `.remove(element)` | Removes first occurrence of element | `playlist.remove("Song1")` | boolean |
| `.remove(index)` | Removes element at specific index | `playlist.remove(0)` | Object |
| `.removeFirst()` | Removes first element | `playlist.removeFirst()` | Object |
| `.removeLast()` | Removes last element | `playlist.removeLast()` | Object |
| `.get(index)` | Gets element at index | `playlist.get(0)` | Object |
| `.getFirst()` | Gets first element | `playlist.getFirst()` | Object |
| `.getLast()` | Gets last element | `playlist.getLast()` | Object |
| `.size()` | **Returns number of elements** | `playlist.size()` | int |
| `.isEmpty()` | Checks if collection is empty | `playlist.isEmpty()` | boolean |
| `.contains(element)` | Checks if element exists | `playlist.contains("Song1")` | boolean |
| `.clear()` | Removes all elements | `playlist.clear()` | void |
| `.indexOf(element)` | Gets index of element | `playlist.indexOf("Song1")` | int |

---

## ArrayList Commands Reference

| Command | Description | Example | Return Type |
|---------|-------------|---------|-------------|
| `.add(element)` | Adds element to end | `list.add("item")` | boolean |
| `.add(index, element)` | Inserts at specific position | `list.add(0, "item")` | void |
| `.set(index, element)` | Replaces element at index | `list.set(0, "new")` | Object |
| `.remove(index)` | Removes element at index | `list.remove(0)` | Object |
| `.remove(element)` | Removes first occurrence | `list.remove("item")` | boolean |
| `.get(index)` | Gets element at index | `list.get(0)` | Object |
| `.size()` | **Returns number of elements** | `list.size()` | int |
| `.isEmpty()` | Checks if empty | `list.isEmpty()` | boolean |
| `.contains(element)` | Checks if exists | `list.contains("item")` | boolean |
| `.clear()` | Removes all elements | `list.clear()` | void |
| `.sort(comparator)` | Sorts the list | `list.sort(null)` | void |

---

## HashMap Commands Reference

| Command | Description | Example | Return Type |
|---------|-------------|---------|-------------|
| `.put(key, value)` | Adds/updates key-value pair | `map.put("name", "John")` | Object |
| `.get(key)` | Gets value for key | `map.get("name")` | Object |
| `.getOrDefault(key, default)` | Gets value or default if not found | `map.getOrDefault("age", 0)` | Object |
| `.remove(key)` | Removes key-value pair | `map.remove("name")` | Object |
| `.remove(key, value)` | Removes only if value matches | `map.remove("name", "John")` | boolean |
| `.containsKey(key)` | Checks if key exists | `map.containsKey("name")` | boolean |
| `.containsValue(value)` | Checks if value exists | `map.containsValue("John")` | boolean |
| `.size()` | Returns number of entries | `map.size()` | int |
| `.isEmpty()` | Checks if empty | `map.isEmpty()` | boolean |
| `.clear()` | Removes all entries | `map.clear()` | void |
| `.keySet()` | Gets all keys | `map.keySet()` | Set |
| `.values()` | Gets all values | `map.values()` | Collection |
| `.entrySet()` | Gets all key-value pairs | `map.entrySet()` | Set |
| `.putAll(map)` | Adds all from another map | `map.putAll(otherMap)` | void |
| `.replace(key, value)` | Replaces value if key exists | `map.replace("name", "Jane")` | Object |

**Note**: `HashMap` is unordered. For ordered maps, use `LinkedHashMap` or `TreeMap`.

---

## HashSet Commands Reference

| Command | Description | Example | Return Type |
|---------|-------------|---------|-------------|
| `.add(element)` | Adds element (no duplicates) | `set.add("apple")` | boolean |
| `.remove(element)` | Removes element | `set.remove("apple")` | boolean |
| `.contains(element)` | Checks if element exists | `set.contains("apple")` | boolean |
| `.size()` | Returns number of elements | `set.size()` | int |
| `.isEmpty()` | Checks if empty | `set.isEmpty()` | boolean |
| `.clear()` | Removes all elements | `set.clear()` | void |
| `.addAll(collection)` | Adds all from collection | `set.addAll(list)` | boolean |
| `.removeAll(collection)` | Removes all from collection | `set.removeAll(list)` | boolean |
| `.retainAll(collection)` | Keeps only common elements | `set.retainAll(list)` | boolean |
| `.iterator()` | Gets iterator | `set.iterator()` | Iterator |

**Note**: `HashSet` doesn't maintain order. Use `LinkedHashSet` for insertion order or `TreeSet` for sorted order.

---

## Quick Pseudocode Examples

### List Example
```
List<String> list = new ArrayList<>()
list.add("apple")
list.add("banana")
list.add(0, "orange")       // Insert at beginning
print list.get(1)           // Output: banana
list.remove("apple")
print list.size()           // Output: 2
```

### LinkedList Example
```
LinkedList<String> songs = new LinkedList<>()
songs.add("Song1")
songs.addFirst("Intro")     // Add at beginning
songs.addLast("Song2")      // Add at end
print songs.getFirst()      // Output: Intro
songs.removeFirst()
print songs.size()          // Output: 2
```

### HashMap Example
```
HashMap<String, Integer> ages = new HashMap<>()
ages.put("Alice", 20)
ages.put("Bob", 25)
ages.put("Charlie", 30)
print ages.get("Bob")       // Output: 25
if ages.containsKey("Alice") then:
    print "Found Alice"
ages.remove("Bob")
print ages.size()           // Output: 2
```

### HashSet Example
```
HashSet<String> fruits = new HashSet<>()
fruits.add("apple")
fruits.add("banana")
fruits.add("apple")         // Duplicate, won't be added
print fruits.size()         // Output: 2
if fruits.contains("apple") then:
    print "Apple exists"
fruits.remove("banana")
print fruits                // Output: {apple}
```

---

## Iteration Method

```java
for(String song : playlist) {
    System.out.println(song);
}
```
---

**Remember**: Always check `.size()` and `.isEmpty()` before accessing elements to avoid `IndexOutOfBoundsException`! 🚀
