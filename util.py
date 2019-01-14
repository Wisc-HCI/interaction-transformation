def remove_traj_loop_helper(traj, length):

    if length == 0:
        return traj
    else:

        start_idx_1 = 0
        start_idx_2 = length
        idxs_to_remove = []
        while True:

            if start_idx_2 + length > len(traj):
                break

            if traj.comparable_component_string(start_idx_1,length) == traj.comparable_component_string(start_idx_2,length):
                idxs_to_remove.append(start_idx_2)
                start_idx_1 += length
                start_idx_2 += length
            else:
                start_idx_1 += 1
                start_idx_2 += 1

        rev_sorted_idxs_to_remove = sorted(idxs_to_remove, key=int, reverse=True)
        for idx in rev_sorted_idxs_to_remove:
            traj.eliminate_section(idx,idx+length)

        return remove_traj_loop_helper(traj,length-1)
