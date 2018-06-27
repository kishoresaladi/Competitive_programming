 public static boolean isBalanced(BinaryTreeNode treeRoot) {

       
        int lh; 
  
        int rh;
  
        
        if (treeRoot== null)
            return true;
  
        lh = height(treeRoot.left);
        System.out.println(lh);
        
        rh = height(treeRoot.right);
         System.out.println(rh);
        if (Math.abs(lh - rh) <= 1  && isBalanced(treeRoot.left)  && isBalanced(treeRoot.right)) 
            return true;
  
        return false;
    }
  
   
   public static int height(BinaryTreeNode treeRoot) 
    {
        
        if (treeRoot == null)
            return 0;
  
        
        return 1 + Math.max(height(treeRoot.left), height(treeRoot.right));
    }
  
        