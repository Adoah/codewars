import java.lang.Math;

public class DeltaBits
{
	static int ms = 0;
	public static int convertBits(int a, int b)
	{
		String aBits = Integer.toBinaryString(a);
		String bBits = Integer.toBinaryString(b);
		ms = maxSize(aBits, bBits);
		aBits = padding(aBits);
		bBits = padding(bBits);
		System.out.println(aBits + ", " + bBits);
		return diffInStrings(aBits, bBits);
	}

	public static String padding(String input)
	{
		String result = "";
		for(int i = 0; i < ms - input.length(); i++)
		{
			result = result + "0";
		}
		return(result + input);
	}
	private static int diffInStrings(String a, String b)
	{
		int diffCount = 0;
		for(int i = 0; i < ms; i++)
		{
			if(a.charAt(i) != b.charAt(i))
			{
				diffCount++;
			}
		}
		return diffCount;
	}
	private static int maxSize(String a, String b)
	{
		if(a.length() > b.length()){return a.length();}
		else{return b.length();}
	}
}
