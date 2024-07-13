
#### `docs/allocation_algorithm.md`

```markdown
# Room Allocation Algorithm

## Overview

The room allocation algorithm is designed to assign rooms to groups in a way that maximizes the number of group members staying together, adheres to gender-specific accommodations, and does not exceed room capacities.

## Steps

1. **Sort Hostels by Capacity**

   The hostels are sorted in descending order by their room capacity. This allows larger groups to be accommodated first, making efficient use of space.

2. **Group by Gender**

   The hostels are grouped by gender to ensure that boys and girls stay in their respective hostels.

3. **Sort Groups by Size**

   Groups are sorted in descending order by their size. This ensures that larger groups are prioritized in the allocation process.

4. **Allocate Rooms**

   - For each group, identify the suitable hostels based on the group's gender.
   - Check if the group's size can be accommodated in any available room.
   - If a suitable room is found, allocate the group to that room and reduce the room's available capacity.
   - If no single room can accommodate the group, handle the case appropriately (e.g., split the group across multiple rooms or provide alternative accommodation).

## Example

Consider a group of 5 boys and two hostels with the following capacities:
- Boys Hostel A: Room 101 (Capacity: 3), Room 102 (Capacity: 4)
- Girls Hostel B: Room 201 (Capacity: 2), Room 202 (Capacity: 5)

The algorithm will allocate the boys to Boys Hostel A, Room 102, as it has the capacity to accommodate all 5 boys.
