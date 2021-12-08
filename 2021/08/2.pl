#!/usr/bin/perl

my $total=0;
my $ns=0;
while (<>)
{ #per linje..:
    @input=split /\|/;

    @res=split(" ",@input[0]);

    my @fwd;
    my %rev;

    
    # finn mapping, først de enkle (1,4,7,8):
    foreach my $out (@res)
    {
	$sout = join "", sort split //, $out;
	$out=$sout;
	my $len=length($out);
	
	if ($len == 2) 
	{
	    $fwd[1]=$out;
	    $rev{$out}=1;
	    $ns++;
	} 
	if ($len == 4)
	{
	    $fwd[4]=$out;
	    $rev{$out}=4;
	    $ns++;
	}
	if ($len == 3)
	{
	    $fwd[7]=$out;
	    $rev{$out}=7;
	    $ns++;
	}
	if ($len == 7)
	{
	    $fwd[8]=$out;
	    $rev{$out}=8;
	    $ns++;
	}
    }
    # så de litt mer komplekse


    #  9:
    foreach my $out (@res)
    {
	my $len=length($out);
	
	if ($len == 6) 
	{
	    $x=$fwd[4];
	    $overlap = () = $out =~ /[$x]/g;
#	    print "9len: $len, $out $x $fwd[4] $overlap\n";
	    if ($overlap == 4)
		{
		    $fwd[9]=$out;
		    $rev{$out}=9;
#		    print "found 9: $out\n";
		}
	}
    }
    # så 0:
    foreach my $out (@res)
    {
	my $len=length($out);
	
	if ($len == 6) 
	{
	    $x=$fwd[1];
	    $overlap = () = $out =~ /[$x]/g;
#	    print "0len: $len, $out $x $fwd[1] $overlap $rev{$out}\n";
	    if ($overlap == 2 && $rev{$out} != 9)
		{
		    $fwd[0]=$out;
		    $rev{$out}=0;
#		    print "found 0: $out\n";
		}
	}
    }

    # 6: 
    foreach my $out (@res)
    {
	my $len=length($out);
	
	if ($len == 6) 
	{
	    $x=$fwd[7];
	    $overlap = () = $out =~ /[$x]/g;
#	    print "0len: $len, $out $x $fwd[7] $overlap $rev{$out}\n";
	    if ($overlap == 2)
	    {

		    $fwd[6]=$out;
		    $rev{$out}=6;
#		    print "found 6: $out\n";
	    }
	}
    }

    
        # så 3,2,5:
    foreach my $out (@res)
    {
	my $len=length($out);
	
	if ($len == 5) 
	{
	    # 3 overlapper 1 med 2
	    $x=$fwd[1];
	    $overlap = () = $out =~ /[$x]/g;
#	    print "3len: $len, $out $x $fwd[1] $overlap $rev{$out}\n";
	    if ($overlap == 2)
		{
		    $fwd[3]=$out;
		    $rev{$out}=3;
#		    print "found 3: $out\n";
		}
	    #2 overlapper 4 med 2
	    $x=$fwd[4];
	    $overlap = () = $out =~ /[$x]/g;
#	    print "2len: $len, $out $x $fwd[4] $overlap $rev{$out}\n";
	    if ($overlap == 2)
		{
		    $fwd[2]=$out;
		    $rev{$out}=2;
#		    print "found 2: $out\n";
		}
	    $x=$fwd[6];
	    $overlap = () = $out =~ /[$x]/g;
#	    print "5len: $len, $out $x $fwd[6] $overlap $rev{$out}\n";
	    if ($overlap == 5)
		{
		    $fwd[5]=$out;
		    $rev{$out}=5;
#		    print "found 5: $out\n";
		}

	}
    }

    @vs= keys %rev;
    
# print "fwd: @fwd vs= @vs $rev{'fg'}\n";

    @outs=split(" ",@input[1]);
    my $rs;
    foreach my $od (@outs)
    {
	$sod = join "", sort split //, $od;
	$od=$sod;

	
	print "$rev{$od}";
	$rs .= $rev{$od};
    }
    print "-$rs\n";
    $total+=$rs;

}
print "total: $total\n";
