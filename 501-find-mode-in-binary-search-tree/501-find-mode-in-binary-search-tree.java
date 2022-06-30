/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private HashMap<Integer, Integer> map = new HashMap<>();
    
    public int[] findMode(TreeNode root) {
        postorder(root);
        int m = Collections.max(map.values());
        return map.entrySet().stream().filter(e -> e.getValue() == m).mapToInt(v -> v.getKey()).toArray();
    }
    
    void postorder(TreeNode node){
        if (node.left != null) postorder(node.left);
        if (node.right != null) postorder(node.right);
        
        map.put(node.val, map.getOrDefault(node.val, 0) + 1);
    }
}