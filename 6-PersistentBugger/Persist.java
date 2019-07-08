class Persist
{
	static int count = 0;
	public static int persistence(long n)
	{
		String numStr = String.valueOf(n);
		int result = 1;
		for(int i = 0; i < numStr.length(); i++)
		{
			result = result * Character.getNumericValue(numStr.charAt(i));
		}
		if(((int) (Math.log10(result) + 1)) == 1){return count + 1;}
		else
		{
			count++;
			return persistence(result);
		}
	}
}
