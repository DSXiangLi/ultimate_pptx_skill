def quicksort(arr):
    """
    快速排序算法
    时间复杂度: 平均 O(n log n), 最坏 O(n²)
    空间复杂度: O(log n) - 递归栈空间
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


# 原地快排（更省内存）
def quicksort_inplace(arr, low=0, high=None):
    """原地快速排序，不创建新数组"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)
    return arr


def partition(arr, low, high):
    """分区函数"""
    pivot = arr[high]  # 选最后一个元素作为基准
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90, 88, 5]
    print(f"原始数组: {test_arr}")
    
    # 方法1: 返回新数组
    sorted_arr = quicksort(test_arr.copy())
    print(f"快排结果: {sorted_arr}")
    
    # 方法2: 原地排序
    arr_copy = test_arr.copy()
    quicksort_inplace(arr_copy)
    print(f"原地快排: {arr_copy}")
